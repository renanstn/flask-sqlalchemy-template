import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

if os.environ.get("FLASK_ENV") == "development":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

db = SQLAlchemy(app)
