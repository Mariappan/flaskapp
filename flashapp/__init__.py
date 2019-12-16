import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flashapp.debug import trace_print
from flashapp.routes import add_routes

trace_print(f"Importing app/__init__")


def create_app(test_config=None):
    # create and configure the flashapp
    _app = Flask(__name__, instance_relative_config=True)
    _app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(_app.instance_path, "flask.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        _app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        _app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(_app.instance_path)
    except OSError:
        pass

    return _app


app = create_app()

db = SQLAlchemy(app)
app.config["myapp-db"] = db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<Member {}>'.format(self.member_name)


add_routes(app, db)
