# Write a class to hold player information, e.g. what room they are in
# currently.

# Default, no items!


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items

    def getItem(self, item):
        self.items.append(item)
    def travel(self, direction):
        if direction in ["n", "s", "e", "w"]:
            next_room = self.current_room.get_room_in_direction(direction)