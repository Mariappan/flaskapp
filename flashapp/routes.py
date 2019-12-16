import uuid

from flask import render_template, Flask, send_from_directory, jsonify, flash
from werkzeug.utils import redirect

from flashapp.model import add_models
from flashapp.config import APP_STATIC
from flashapp.debug import trace_print, debug_print
from flashapp.forms import MemberForm
from flashapp.utils import routes

import flashapp.temp_routes  # Don't DELETE this one

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


DB = None
Models = None


@routes("/members", "members", methods=["GET", "POST"])
def _members():
    form = MemberForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.member_name.data, form.member_age.data))
        member = Models.Member(member_name=form.member_name.data, member_age=form.member_age.data)
        DB.session.add(member)
        DB.session.commit()
        return redirect('/members')

    members = DB.session.query(Models.Member).all()
    return render_template('members.htm', title='Members', form=form, members=members)


def add_routes(app: Flask, db):
    global DB, Models
    DB = db
    Models = add_models(app, db)

    # Create tables for our models
    db.create_all()

    for route in routes.all:
        debug_print(f"Adding route: {route}")
        *route, methods = route
        app.add_url_rule(*route, methods=methods)
