from flask import Blueprint, jsonify

class Dessert:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

desserts_list = [
    Dessert(1, "tres leches cake", "Nick Lachey cake"),
    Dessert(2, "red velvet cake", "red food coloring, fake cake"),
    Dessert(3, "sweet potato pie", "healthy, better than pumpkin, best made by endearing loving aunt or grandma")
]

desserts_bp = Blueprint("desserts", __name__, url_prefix="/desserts")

browse_bp = Blueprint("browse",__name__, url_prefix="/browse")

main_path = "www.nordstrom.com"

@browse_bp.route("/womens", methods=["GET"])
def handle_womens_items():
    # create function to display all womens items data
    return "Womens Items Route"


#www.nordstrom.com/browse/womens <-- endpoint we plop into postman to test



@desserts_bp.route("", methods=["GET"])
def handle_desserts():
    # describe response for displaying all desserts
    desserts_response = []
    for dessert in desserts_list:
        desserts_response.append(
            {
                "id": dessert.id,
                "name": dessert.name,
                "description": dessert.description
            }
        )

    return jsonify(desserts_response)

@desserts_bp.route("/<dessert_id>", methods=["GET"])
def handle_dessert(dessert_id):
    dessert_id = int(dessert_id)
    for dessert in desserts_list:
        if dessert.id == dessert_id:
            return {
                "id": dessert.id,
                "name": dessert.name,
                "description": dessert.description
            }

    return jsonify("id not found"), 404 # how to return 404 code 
    # Returning status codes, can be found in More Flask lesson in "404s and More Queries"
        


