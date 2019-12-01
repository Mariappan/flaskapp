import functools
import uuid
from flask import render_template, Flask, send_from_directory, jsonify

from flashapp.config import APP_STATIC
from flashapp.debug import trace_print, debug_print
from flashapp.utils import routes

import flashapp.temp_routes

trace_print(f"Importing app/routes")


@routes("/favicon.ico", "favicon.ico")
def favicon():
    return send_from_directory(
        APP_STATIC, "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


@routes("/", "index")
@routes("/index", "index")
def _index():
    user = {"username": "David Christ"}
    return render_template("index.htm", title="Home", user=user)


@routes("/hello", "hello", methods=["GET", "POST"])
def _hello():
    return f"Hello, World!"


@routes("/uuid", "uuid")
def _uuid():
    return render_template("uuid.htm", title="UUID")


@routes("/generate_uuid", "uuid_gen", methods=["POST"])
def _generate_uuid():
    return jsonify({"uuid": uuid.uuid4()})


def add_routes(app: Flask):
    for route in routes.all:
        debug_print(f"Adding route: {route}")
        *route, methods = route
        app.add_url_rule(*route, methods=methods)
