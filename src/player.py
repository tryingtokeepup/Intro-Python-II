# Write a class to hold player information, e.g. what room they are in
# currently.

# Default, no items!


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.current_items = items

    def getItem(self, item):
        self.current_items.append(item)
