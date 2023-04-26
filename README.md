<h1 align="center">Raspar notícias de tecnologia</h1>

<p align="center">
    <img src="/.imgs/tech-news.png" width="100%" />
</p>

## Sobre o projeto

Realiza consultas em nóticias sobre tecnologia e armazena os dados em um banco de dados MongoDB. 
Utiliza o site [blog da Trybe](https://blog.betrybe.com/) para realizar a raspagem de dados.

## Tecnologias utilizadas

-   [Python](https://www.python.org/) - Linguagem de programação interpretada de alto nível.
-   [Requests](https://docs.python-requests.org/en/master/) - Biblioteca Python HTTP para humanos.
-   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Biblioteca Python para extrair dados de arquivos HTML e XML.
-   [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Biblioteca Python para trabalhar com o MongoDB.
-   [Pytest](https://docs.pytest.org/en/7.2.x/) - Framework de testes em Python.

## Funcionalidades

- Realizar requisição HTTP.
- Realizar raspagem de dados.
- Armazenar as notícias em um banco de dados MongoDB.
- Recuperar as notícias do banco de dados.
- Script de raspagem de dados.

## Instalação

```bash
# Clonar Projeto
$ git clone git@github.com:lucas-da-silva/scrape-tech-news.git

# Entrar no diretório
$ cd scrape-tech-news

# Criar ambiente virtual e ativá-lo
$ python3 -m venv .venv && source .venv/bin/activate

# Instalar dependências
$ python3 -m pip install -r dev-requirements.txt

# Subir o banco de dados
$ docker-compose up -d mongodb

# Executar a raspagem de dados
$ tech-news-analyzer

# Executar testes
$ python3 -m pytest
```

## Estrutura do projeto

```
$PROJECT_ROOT
|   # Arquivos de raspagem de dados
├── tech_news
|   |   # Funções que acessam e recuperam dados do banco de dados 
│   └── analyzer
|   # Arquivos de testes
└── tests
    |   # Arquivos de mocks
    |-- mocks
    |   # Testes da função group_news_for_available_time
    └── reading_plan

```

## Autor

-   [@lucas-da-silva](https://github.com/lucas-da-silva)
