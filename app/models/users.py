from dataclasses import field
import datetime
from app import db, ma

class Users(db.Model):
    """ Definição da classe usuário e seus campos """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','username','password','name', 'created_on')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)