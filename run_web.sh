#!/usr/bin/env bash

#criando ambiente virtual.
python3 -m venv myvenv

#ativando ambiente virtual.
source myvenv/bin/activate

#atualizando o pip.
pip install --upgrade pip

#Django não suporta servir arquivos estáticos na produção. No entanto, o fantástico projeto WhiteNoise pode ser integrado ao seu aplicativo Django e foi projetado exatamente com esse objetivo em mente. Veja a documentação do WhiteNoise para mais detalhes.
pip install django whitenoise

#Acessar diretório do projeto
cd src

python -m pip install Pillow

#Isso irá copiar todos os arquivos dos seus diretórios estáticos para dentro do diretório definido em STATIC_ROOT.
python manage.py collectstatic --noinput

#migrando o banco de dados.
python manage.py migrate

#criando o super usuário do para administração via web.
python manage.py createsuperuser

#rodando servidor web na porta 8000.
python manage.py runserver 0.0.0.0:8000

