from distutils.debug import DEBUG


DEBUG = True

#Database Settings
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/database"
SQLALCHEMY_TRACK_MODIFICATIONS = False