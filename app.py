"""
Definition of main Flask Application.

Authors: Handerson Contreras.
"""
from flask import Flask 
from flask import render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

APP = Flask(__name__)
APP.config.from_pyfile('prod.cfg')

API = Api(APP)
DB = SQLAlchemy(APP)
MA = Marshmallow(APP)

from api.users import *
from models.user import User
