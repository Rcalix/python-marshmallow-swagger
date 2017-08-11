"""
User Model

Authors: Handerson Contreras
"""
from app import DB

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(60), unique=True)
    first_name = DB.Column(DB.String(50))
    last_name = DB.Column(DB.String(50))

