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
