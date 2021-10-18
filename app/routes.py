from flask import Blueprint, jsonify

class Dessert:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

