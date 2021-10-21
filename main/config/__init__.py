"""  
Configurations
"""
import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

# :::::::: ENVIRONMENT  Config :::::::::::::::::
load_dotenv()
load_dotenv(dotenv_path=Path(".") / ".env")
# :::::::::: APP INITIALIZATION ::::::::::::::::
app = Flask(__name__, template_folder="../templates")

# :::::::: General  app Configuration:::::::::::
app.config["QR_CODE_FOLDER"] = os.environ["QR_CODE_FOLDER"]
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=4)

# ::::::::: SQLAlchemy configuration :::::::::::
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["TEST_DB"]

database = SQLAlchemy(app)

# :::::::: SECURITY CONFIG ::::::::::::::::::::
CORS(app)
jwt = JWTManager(app)
AUTH_SECURITY_KEY = os.environ["SECURITY_KEY"]
from main import controller

