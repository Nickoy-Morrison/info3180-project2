from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf = CSRFProtect(app)

bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = "this is a super secure key"  # you should make this more random and unique
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fvygwiavhypvsv:61a032f0a3c94589855fb4f2a37038b7f1bb2eb661653c58261e6bdff6bdf9f3@ec2-54-83-205-27.compute-1.amazonaws.com:5432/d1l7tft5g9sd5g"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project:password123@localhost/project"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # added just to suppress a warning

UPLOAD_FOLDER ='./app/static/uploads'
PROFILE_IMG_UPLOAD_FOLDER = os.path.join("static/uploads", "profile_photos")
POST_IMG_UPLOAD_FOLDER = os.path.join("static/uploads", "posts")

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
