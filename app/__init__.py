from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

app = Flask(__name__ )
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db )
mail = Mail(app)



from Gsign.G_auth import *
from app import routes, models
