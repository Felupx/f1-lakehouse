# 🏎️ F1 Lakehouse

Projeto de engenharia de dados para coleta, armazenamento e processamento de dados da Fórmula 1, com foco na construção de pipelines analíticos e preparação para modelos preditivos.

## 📌 Sobre o Projeto
Este projeto tem como objetivo implementar, na prática, uma arquitetura Lakehouse, passando por todas as etapas de um pipeline de dados:

- Coleta de dados via API
- Armazenamento em formato bruto
- Processamento e transformação dos dados
- Organização em camadas analíticas
- Preparação para Machine Learning

O desenvolvimento é baseado em estudos práticos de engenharia de dados, com adaptação e implementação própria dos conceitos.

## 🧠 Etapas do Projeto

- [Coleta](#coleta)
- [Armazenamento dos Dados](#armazenamento-dos-dados)
- [Camada Bronze](#camada-bronze)
- [Camada Silver](#camada-silver)
- [Camada Gold](#camada-gold)
- [Modelagem de Dados](#modelagem-de-dados)
- [Visualização e Aplicação](#visualização-e-aplicação)

### 📥 Coleta

A coleta de dados é realizada utilizando a biblioteca FastF1, responsável por fornecer dados históricos e de sessões da Fórmula 1.

O processo é feito via scripts em Python, estruturados para permitir reutilização e expansão do pipeline.

### 💾 Armazenamento dos Dados

Na camada bronze, nossos dados estarão consolidados em formato `Delta` com histórico de modificações, facilitando suas consultas. Além disso, teremos uma representação fiel de como este dado poderia ser encontrado em sua origem.

### 🥉 Camada Bronze

Nesta camada, os dados são armazenados em sua forma bruta, mantendo fidelidade total à origem.

O objetivo é preservar os dados originais para:

- Reprocessamento futuro
- Auditoria
- Rastreabilidade

### 🥈 Camada Silver

A camada Silver é responsável pelo tratamento e padronização dos dados.

Aqui são realizadas operações como:

- Limpeza de dados
- Padronização de colunas
- Tratamento de valores nulos
- Ajustes de tipos de dados

### 🥇 Camada Gold

Na camada Gold, os dados são organizados para consumo analítico.

São geradas tabelas mais estruturadas, focadas em:

- Análises
- Consultas
- Integração com dashboards

### 🤖 Modelagem de Dados

Com os dados organizados, o próximo passo é a construção de bases analíticas (ABT - Analytical Base Table), que servirão de base para modelos de Machine Learning.

### 📊 Visualização e Aplicação

Futuramente, será desenvolvida uma aplicação para visualização dos dados e possíveis predições, utilizando ferramentas como:

- Streamlit
- Dashboards interativos

## ⚙️ Tecnologias Utilizadas
- Python
- Pandas
- FastF1
- Parquet
- Git & GitHub

(em evolução: AWS, MLFlow, Streamlit)

## 🚀 Objetivo

Mais do que apenas replicar um projeto, o foco é consolidar conhecimentos em:

- Engenharia de Dados
- Estruturação de pipelines reais
- Organização de projetos profissionais
- Preparação para o mercado de dados