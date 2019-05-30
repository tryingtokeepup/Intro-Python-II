# Write a class to hold player information, e.g. what room they are in
# currently.

# Default, no items!


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items

    def get_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        # so we need to be able to have the user type in the item they want to drop
        # and then traverse the array of items and drop it
        for i in self.items:
            if self.items[i] == item:
                self.items.pop(i)

    def travel(self, direction):

        next_room = self.current_room.getRoomInDirection(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print(
                "You are determined, but the wall does not yield. You cannot go that way.\n")
