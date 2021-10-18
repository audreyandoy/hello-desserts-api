from flask import Blueprint, jsonify

class Dessert:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

# from Delish's fall dessert recipes
desserts = [
    Dessert(1, "Caramel Apple Pie", "Classic apple pie drizzled with caramel"),
    Dessert(2, "Apple Cider Doughnuts", "Sweet, airy doughnuts served with blueberry-ginger jam"),
    Dessert(3, "Pumpkin Chocolate Chip Cookies", "Soft, chewy chocolate chip cookies with a hint of pumpkin")
]


hello_world_bp = Blueprint("hello_bp", __name__)
desserts_bp = Blueprint("desserts_bp", __name__, url_prefix="/desserts")


@desserts_bp.route("", methods=["GET"])
def handle_desserts():
    desserts_response = []
    for dessert in desserts:
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
    for dessert in desserts:
        if dessert.id == dessert_id:
            return {
                "id": dessert.id,
                "title": dessert.title,
                "description": dessert.description,
            }


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

