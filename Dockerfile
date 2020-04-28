############################################################
# Dockerfile configurar o ambiente de desenvolvimento Phyton
############################################################

# Container base: python latest
FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /usr/src/app

# "Copia" arquivo requirements.txt para o diretorio Python
COPY requirements.txt ./

# Executa o pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m pip install Pillow

# "Copia" os arquivos locais para o diretorio Python no container 
COPY . .

# Django service
EXPOSE 8000

