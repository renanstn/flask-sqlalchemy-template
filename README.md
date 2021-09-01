# flask-sqlalchemy-template

Template de uma aplicação Flask, utilizando SQLAlchemy como ORM, e Alembic como ferramenta de migrations.

## Comandos

### Criar migrations

```
alembic revision --autogenerate -m "<fixture name>"
```

### aplicar migrations

```
alembic upgrade head
```
