import os
from flask import Flask 
from flask.ext.cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
cache = Cache(app)

from app import ascii, models
from models import * 