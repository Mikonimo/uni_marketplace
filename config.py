import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
          'mysql+pymysql://mikonimo:8a3k5r13@localhost/uni_marketplace'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
