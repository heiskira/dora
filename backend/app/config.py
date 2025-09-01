import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#from dotenv import load_dotenv
#import os

#load_dotenv()

#class Config:
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False