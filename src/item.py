# need to add an item class


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return f"{self.name}"
    def __str__(self):
        return f"{self.name}"