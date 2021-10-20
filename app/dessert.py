class Dessert:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def to_json(self):
        '''
        Helper method to turn object into dictionary
        '''
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }