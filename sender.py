# %%
import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

# %%
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")

# %%