# flask-sqlalchemy-template

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=flat&logo=heroku&logoColor=white)](https://www.heroku.com)

Template de uma aplicação Flask, utilizando SQLAlchemy como ORM, e Alembic como ferramenta de migrations.

## Comandos alembic

### Criar migrations

```
alembic revision --autogenerate -m "<fixture name>"
```

### Aplicar migrations

```
alembic upgrade head
```
