## Projeto
#### Clonar o projeto 
```
git clone git@github.com:giovani77/django_ecomerce.git
```

#### Utilzar a branch
```
git checkout desenv
```

## Ambiente

#### Ir no diretório django_ecomerce
#### Instanciar os contêineres: 
```
docker-compose up -d
```

#### No Windows, durante a configuração o Docker Desktop solicita o compartilhamento dos diretórios. 
#### Entrar com bash no Conteiner, executar no CMD: 
```
docker exec -it django_ecomerce_web_1 bash
```

#### Entrar no diretório /src e dar o comandos abaixo:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser (para criar o usuário máster da aplicação)
```

#### Acessar localhost

http://127.0.0.1:8000/

### Rodar testes unitários
```
 Todos: python3 manage.py test
 Individual: python3 manage.py test pessoa.tests.unit_tests.tests_models.PessoaTestCase.test_nome_sobrenome_invalido_com_espaco
```