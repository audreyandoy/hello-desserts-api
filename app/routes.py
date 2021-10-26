from flask import Blueprint, json, jsonify, request
from app.models.dessert import Dessert 
from app import db


hello_world_bp = Blueprint("hello_bp", __name__)
desserts_bp = Blueprint("desserts_bp", __name__, url_prefix="/desserts")


@desserts_bp.route("", methods=["POST", "GET"])
def handle_desserts():

    if request.method == "POST":
        request_body = request.get_json()

        # guard clause
        if "name" not in request_body or "description" not in request_body:
            return jsonify("Invalid Request"), 400

        new_dessert = Dessert(
            name = request_body["name"],
            description = request_body["description"]
        )

        db.session.add(new_dessert)
        db.session.commit()
        
        return jsonify(f"created {new_dessert.name}"), 201

    elif request.method == "GET":
        desserts = Dessert.query.all()
        desserts_response = [ dessert.to_json() for dessert in desserts]
        print(desserts)
        return jsonify(desserts_response), 200


@desserts_bp.route("/<dessert_id>", methods=["GET"])
def handle_dessert(dessert_id):
    dessert = Dessert.query.get(dessert_id)

    if dessert is None:
        return jsonify(f"Dessert {dessert_id} not found"), 404

    return dessert.to_json()


@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    return "Hello, World!"


@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }

