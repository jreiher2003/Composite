import os
from flask import Flask 
from werkzeug.contrib.fixers import ProxyFix
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from app import ascii, models
from models import * 