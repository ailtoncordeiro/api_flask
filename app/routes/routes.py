from app import app
from flask import jsonify, render_template
from ..views import users

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message":"Welcome!"})

@app.route('/api/docs')
def get_docs():
    print('sendig docs')
    return render_template('swaggerui.html')

@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/users', methods=['GET'])
def get_user():
    return users.get_user()