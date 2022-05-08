from unittest import result
from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def post_user():
    """ Create user """
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

def update_user(id):
    """ Update User """
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    user = Users.query.get(id)
    if not user:
        return jsonify({"message":"User don't exist","data":{}}), 404
    pass_hash = generate_password_hash(password)
    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message":"successfuly updated","data": result}), 201
    except:
        return jsonify({"message":"unable to update","data":{}}), 500

def get_users():
    """ Get all users """
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message":"successfully fetched", "data": result})
    
    return jsonify({"message":"nothing found", "data":{}})

def get_user(id):
    """ Get user """
    users = Users.query.get(id)
    if users:
        result = user_schema.dump(users)
        return jsonify({"message":"successfully fetched", "data": result})
    
    return jsonify({"message":"user don't exist", "data":{}})

def delete_user(id):
    """ Delete User """
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': "user don't exist", 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            result = user_schema.dump(user)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500