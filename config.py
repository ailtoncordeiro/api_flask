import string
import random


#Key
randomString = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(randomString) for i in range(100))
SECRET_KEY = key

#Debug
DEBUG = True

#Database Settings
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/database"
SQLALCHEMY_TRACK_MODIFICATIONS = False