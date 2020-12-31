#!/usr/bin/env bash

#criando ambiente virtual.
python3 -m venv myvenv

#ativando ambiente virtual.
source myvenv/bin/activate

#atualizando o pip.
pip install --upgrade pip

#Django não suporta servir arquivos estáticos na produção. No entanto, o fantástico projeto WhiteNoise pode ser integrado ao seu aplicativo Django e foi projetado exatamente com esse objetivo em mente. Veja a documentação do WhiteNoise para mais detalhes.
pip install django whitenoise

python -m pip install Pillow

#Isso irá copiar todos os arquivos dos seus diretórios estáticos para dentro do diretório definido em STATIC_ROOT.
python src/manage.py collectstatic --noinput

#migrando o banco de dados.
python src/manage.py migrate

#criando o super usuário do para administração via web.
python src/manage.py createsuperuser

#Acessar diretório do projeto
cd src

#rodando servidor web na porta 8000.
python manage.py runserver 0.0.0.0:8000

