############################################################
# Dockerfile configurar o ambiente de desenvolvimento Phyton
############################################################

# Container base: python latest
FROM python:latest

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir -p /webapps

# Define o diretório de trabalho
WORKDIR /webapps

# "Copia" arquivo requirements.txt para o diretorio Python
ADD requirements.txt /webapps/

# Executa o pip
RUN pip install -r requirements.txt

# "Copia" os arquivos locais para o diretorio Python no container 
ADD . /webapps/

# Django service
EXPOSE 8000

