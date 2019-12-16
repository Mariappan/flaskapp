import os

# __file__ refers to the file config.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, "static")

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(APP_ROOT, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
