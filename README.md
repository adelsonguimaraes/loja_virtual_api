# LOJA VIRTUAL API

Uma simples API utilizando Python/Django, possuí apenas um end point com o recurso produto, com operações de Cadastrar, Atualizar, Listar e Deletar, utilizando os verbos Post, Get, Update e Delete.

# Tecnologias
- [python3](https://www.python.org/) Linguagem de programação.
- [Django](https://www.djangoproject.com/) Framework Web Python
- [Django Rest Framework](https://www.django-rest-framework.org/) Ferramenta de construção de API's em Python
- [Postman](https://www.postman.com/) Para consultar a API como client

>Esse projeto foi isolado em um ambiente VENV do python para evitar qualquer problema ou conflito das dependências.

# Instruções para utilizar
Faça o clone do repositório via terminal
>git clone https://github.com/adelsonguimaraes/loja_virtual_api.git

Acesse via terminal o repositório do projeto e siga os passos.

Crie uma máquina virutal VENV com o python.
>python3 -m venv ./venv

Ative a máquina virtual (Windows)
>venv\Scripts\activate.bat

Ative a máquina virtual (Linux)
>source venv\Scripts\activate

Instale o Django Framework
>pip install django

Instale o Django Rest Framework
>pip install djangorestframework

Como estamos utlizando o SQLite, não precisamos nos preocupar com o banco de dados pois o Django criará automaticamente o arquivo, então, vamos apenas executar nossa migrate.
>python manage.py migrate

Inicialize o servidor
>python manage.py runserver

Pronto, agora podemos utilizar alguma ferramenta como o [Postman](https://www.postman.com/) para consumir nossa API, abaixo segue os nossos endpoints.

Listar todos os produtos
>GET http://localhost:8000/produto/

Cadastrar novo produto
>POST http://localhost:8000/produto/

Buscar produto por ID
>GET http://localhost:8000/produto/id/

Atualizar produto
>PUT http://localhost:8000/produto/id/

Remover produto
>DELETE http://localhost:8000/produto/id/

# Documentação de desenvolvimento
Nessa sessão documentei todo o processo utilizado para desenvolver a API com Django, para servir como uma doc de orientação para projetos futuros.
<details>

  <summary>Clique para expandir a seção</summary>

## Configuração de ambiente

Criando ambiente virtual python
>python3 -m venv ./venv

Ativando o ambiente virtual no Windows
>venv\Scripts\activate.bat

Ativando o ambiente virtual no Linux
>source venv\Scripts\activate

Instalando Django dentro do ambiente
>pip install django

Criando um projeto com Django
>django-admin startproject config .

Iniciando o servidor com ``Manage``
>python manage.py runserver

Com isso nosso servidor está rodando, no terminal ele informa o endereço localhost e a porta pra acessar a aplicação via navegador, o padrão é.
>http://localhost:8000

## Configurações do projeto

Alterando a linguagem do projeto para pt-BR,
dentro do arquivo ``/config/settings.py`` alterar a linha 
>LANGUAGE_CODE = 'en-us'

para essa configuração
>LANGUAGE_CODE = 'pt-br'

Vamos modificar o timezone também, mude
>TIME_ZONE = 'UTC'

para essa configuração
>TIME_ZONE = 'America/Manaus'

## Criando Aplicação

Agora que já temos o ``Manage`` configurado e funcionando, vamos criar nossa aplicação, vou chamar de app.
>python manage.py startapp ``app``

Agora vamos criar o model de produto, acessando dentro do diretório da nossa aplicação ``app/models.py``, segue abaixo o código do modelo de produto.
```python
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
```

Nesse modelo de produtos temos um campo ``nome`` do tipo string com máximo aceito de 30 caracteres, um campo ``quantidade`` do tipo inteiro e um campo ``valor`` do tipo decimal que aceita até 19 dígitos inteiros (aproximadamente valores até um bilhão) e 2 casas decimais.

Vamos adicionar também uma representação para esse produto, com o seguinte código

```python
def __str__(self):
  return self.nome
```

## Migrations
Hora de persistir nosso modelo no banco de dados, 
mas primeiro precisamos adicionar nossa aplicação dentro do projeto, para isso vamos acessar o arquivo ``config/settings.py``, e adicionar nosso ``app`` no array de ``INSTALLED_APPS``,  ficando assim.

```python
INSTALLED_APPS = [
    'Django.contrib.admin',
    'Django.contrib.auth',
    'Django.contrib.contenttypes',
    'Django.contrib.sessions',
    'Django.contrib.messages',
    'Django.contrib.staticfiles',
    'app',
]
```
Pronto agora o ``Manage`` vai ser capaz de encontrar nosso ``app`` e criar as migrations, para isso vamos rodar o seguinte comando.

>python manage.py makemigrations

O retorno deve ser algo como
```bash
←[36;1mMigrations for 'app':←[0m
  ←[1mapp\migrations\0001_initial.py←[0m
    - Create model Produto
```
Com isso criamos a migration de produto, agora podemos persistir essa migration no nosso banco de dados, usamos o seguinte comando pra isso.
>python manage.py migrate

## Admin Django

A migration do nosso modelo de Produto agora foi persistida em nosso banco de dados. Vamos aproveitar pra configurar o admin do Django pra que possamos visualizar e testar o nosso modelo. Vamos acessar o arquivo ``app/admin.py`` e vamos importar e registrar nosso modelo adicionando o código a seguir.
```python
from app.models import Produto

class Produtos(admin.ModelAdmin):
  # campos que devem ser exibidos
  list_display = ('id', 'nome', 'rg')
  # campos que seram clicáveis
  list_display_links = ('id', 'nome')
  # campo de busca/filtro
  search_fields = ('nome',)

# registrando a model (model, class)
admin.site.register(Produto, Produtos)
```
Para conseguirmos acessar o admin do Django, precisamos configurar um usuário, para isso utilizamos o comando
>python manage.py createsuperuser

Em seguida será solicitado a inserção de alguns dados como ``usuário``, ``email`` e ``senha``, insira as informações e em seguida vamos acessar o link admin para entrar com os dados cadastrados.
>http://localhost:8000/admin

Agora estamos dentro do painel admin do Django e como registramos nossa model de Produto ela já deve aparecer, podemos adicionar, editar, remover. listar e filtrar por itens.

## Construindo a API
Agora que temos o modelo pronto, banco de dados estruturado, fizemos alguns teste com o admin do Django, vamos começar a criar nossa API. Para isso vamos utilizar uma outra ferramenta chamada [Django Rest Framework](https://www.django-rest-framework.org/).

Inicialmente precisamos instalar no nosso projeto essa ferramenta, então podemos fazer isso utilizando o seguinte código.
>pip install djangorestframework

Após a instalação precisamos adicionar a ``INSTALLED_APPS`` no arquivo ``config/settings.py`` assim como fizemos com a nossa ``app`` anteriormente, então com a atualização devemos ter o seguinte resultado.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'rest_framework',
]
```
Agora precisamos configurar nosso Serializer, responsável por tratar os dados que entram e saem da API, convertendo para JSON na saída e desconvertendo na entrada.

Para isso vamos criar um novo arquivo chamado ``serializer.py`` dentro do nosso diretório ``app`` e dentro desse arquivos vamos adicionar o seguinte conteúdo.
```python
# importando o serialize da ferramenta
from rest_framework import serializers
# importanto o nosso modelo
from app.models import Produto

# classe de serialização, com serializador de modelo
class ProdutoSerializer(serializers.ModelSerializer):
  # meta, onde configuramos o modelo e
  # os campos que queremos serializar
  class Meta:
    model = Produto
    fields = ['id','nome','quantidade', 'valor']
```

Com nosso serializador pronto, vamos agora trabalhar nas ``views``.
>No Django as ``Views`` fazem um papel semelhante ao que as ``Controllers`` fazem em outras ferramentas.

Agora vamos acessar o arquivo ``app/views`` e configurar a saída dos nossos dados, por padrão a ``view`` vem preparada para renderizar uma página, porém no nosso caso vamos apenas retornar dados de nossa API, então vamos substituir o conteúdo, vamos inciar fazendo os imports.
```python
# importando httpResponse e JsonResponse
from django.http import HttpResponse, JsonResponse
# importando o decorator csrf_exempt
from django.views.decorators.csrf import csrf_exempt
# importanto o json parse
from rest_framework.parsers import JSONParser
# importando model produto
from app.models import Produto
# importando serializador de produto
from app.serializer import ProdutoSerializer
```

Em seguida vamos criar uma função que contempla nosso GET para listar tudo e POST para cadastrar.
```python
# removendo o csrf
@csrf_exempt
# função list que contém o getAll e o Create
def produto_list(request):
  if request.method == 'GET':
    produtos = Produto.objects.all()
    serializer = ProdutoSerializer(produtos, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ProdutoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
```

E por último vamos adicionar uma outra função que vai receceber um id e vai comtemplar os verbos GET buscar por id, PUT atualizar por id e DELETE remover por id.
```python
@csrf_exempt
# função detail que recebe contém GET, PUT e DELETE
# necessitando da passagem do parámetro ID
def produto_detail(request, pk):

  # verificando ser o produto existe via id
  try:
    produto = Produto.objects.get(pk=pk)
  except Produto.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ProdutoSerializer(produto)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = ProdutoSerializer(produto, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.erros, status=400)

  elif request.method == 'DELETE':
    produto.delete()
    return HttpResponse(status=204)
```

Vamo criar agora dentro ``app`` nosso arquivo de urls e dentro vamos adicionar a chamada da model.
```python
from django.urls import path
from app import views

urlpatterns = [
    path('produto/', views.produto_list),
    path('produto/<int:pk>/', views.produto_detail),
]
```

E precisamos incluir nossas urls dentra das urls  do projeto em ``config/url``, ficando assim.
```python
# importando o admin do django
from django.contrib import admin
# importando o path e include do modulo urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # adicionando as urls de app
    path('', include('app.urls')),
]
```
Nossas rotas estão configuradas, agora podemos fazer requisições para nossa API.

Listar todos
>GET http://localhost:8000/produto/

Cadastrar
>POST http://localhost:8000/produto/

Buscar por ID
>GET http://localhost:8000/produto/id/

Atualizar
>PUT http://localhost:8000/produto/id/

Remover
>DELETE http://localhost:8000/produto/id/

## Gitignore
Vamos criar nosso no arquivo ``.gitignore`` na raiz do projeto e configurar o que não queremos enviar para o repositório, com o seguinte conteúdo.
```gitbash
*.pyc  
*~  
__pycache__  
venv  
db.sqlite3  
/static  
.DS_Store
```

</details>

# Referências
Aqui segue as referências que utilizei para a realização desse projeto.

- [Criando uma API com Django](https://www.youtube.com/watch?v=BKChTO8GADk) - Youtube Alura Cursos
- [Django Framework](https://docs.djangoproject.com/en/3.2/) - Documentação Django
- [Django Rest Framework](https://www.django-rest-framework.org/) - Documentação Django Rest

# Autor
- Adelson Guimarães Monteiro
- Analista Jr de Sistemas / FullStack
- [Linkedin](https://www.linkedin.com/in/adelson-guimaraes-31b31a26/): Minha rede
- [Github](https://github.com/adelsonguimaraes): Meus projetos