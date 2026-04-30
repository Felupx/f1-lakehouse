# %%
import argparse
import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

from tqdm import tqdm

load_dotenv()

# %%

class Sender:

    def __init__(self, container_name: str, folder: str):
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.container_name = container_name
        self.folder = folder

        self.blob_service_client = BlobServiceClient.from_connection_string(
            self.connection_string
        )

        self.container_client = self.blob_service_client.get_container_client(
            self.container_name
        )

    def process_file(self, filename: str):

        file = os.path.basename(filename)
        blob_path = f"{self.folder}/{file}"

        try:
            with open(filename, "rb") as data:
                self.container_client.upload_blob(
                    name=blob_path,
                    data=data,
                    overwrite=True
                )

        except Exception as err:
            print(f"Erro ao enviar {filename}: {err}")
            return False

        # só chega aqui se deu certo
        os.remove(filename)
        return True
    
    def process_folder(self, folder: str):
        files = [i for i in os.listdir(folder) if i.endswith(".parquet")]

        for f in tqdm(files):
            filename = os.path.join(folder, f)
            self.process_file(filename)

# %%

parser = argparse.ArgumentParser()
parser.add_argument("--container", type=str)
parser.add_argument("--blob_path", type=str)
parser.add_argument("--folder", default="data", type=str)
args = parser.parse_args()

if args.container:
    send = Sender(args.container, args.blob_path)
    send.process_folder(args.folder)

else:
    print("Container não especificado. Use --container para enviar os arquivos.")