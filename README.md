# flask-sqlalchemy-template

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
