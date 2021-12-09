import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-should-have-been-a-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db');
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    
    
    
    
    # export FLASK_ENV=development
    
    