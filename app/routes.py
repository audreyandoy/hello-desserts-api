from flask import Blueprint, jsonify
from .data import desserts_list

desserts_bp = Blueprint("desserts", __name__, url_prefix="/desserts")

@desserts_bp.route("", methods=["GET"])
def handle_desserts():
    # describe response for displaying all desserts
    desserts_response = []
    for dessert in desserts_list:
        desserts_response.append(dessert.to_json())

    return jsonify(desserts_response)

@desserts_bp.route("/<dessert_id>", methods=["GET"])
def handle_dessert(dessert_id):
    dessert_id = int(dessert_id)
    for dessert in desserts_list:
        if dessert.id == dessert_id:
            return dessert.to_json()

    return jsonify("id not found"), 404 # this is how we can return 404 code 
    # Returning status codes, can be found in More Flask lesson in "404s and More Queries"
        


