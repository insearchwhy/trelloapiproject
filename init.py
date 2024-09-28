from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import flask_marshmallow
from flask_bcrypt import flask_bcrypt
from flask_jwt_extendef import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()