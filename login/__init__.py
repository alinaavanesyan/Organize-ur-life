import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask_migrate import Migrate
csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()

from app import views,models