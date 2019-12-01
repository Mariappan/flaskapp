import uuid
from flask import jsonify

from flashapp.routes import routes


@routes("/temp_gen", "temp_gen", methods=["POST"])
def _temp_gen():
    return jsonify({"gen": uuid.uuid4()})

