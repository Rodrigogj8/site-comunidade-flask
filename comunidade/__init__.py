from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config["SECRET_KEY"] = "ae47ac802046ad5b606d5f957528a83f"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidade import routes, models