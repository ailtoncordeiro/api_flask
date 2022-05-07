from unittest import result
from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def post_user():
    
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name)
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message":"successfully registered", "data": result}), 201
    except:
        return jsonify({"message":"unable to create","data":{}}), 500

def get_user():

    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message":"successfully fetched", "data": result})
    
    return jsonify({"message":"nothing found", "data":{}})

