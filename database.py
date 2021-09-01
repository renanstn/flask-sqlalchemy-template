import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if os.environ.get("FLASK_ENV") == "development":
    database_url = 'sqlite:////tmp/test.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    database_url = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')


engine = create_engine(database_url)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import Project
    Base.metadata.create_all(bind=engine)
