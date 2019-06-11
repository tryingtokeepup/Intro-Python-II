# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
        self.n_to = None  # this will allow a room to connect to this north node
        self.s_to = None  # this will allow a room to connect to this south node
        self.e_to = None  # this will allow a room to connect to this east node
        self.w_to = None  # this will allow a room to connect to this west node

    def add_item(self, item):
        self.items.append(item)

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
        else:
            return None

    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)

    def transferItem(self, itemname, player):
        for index, item in enumerate(self.items):
            pass

    def __repr__(self):
        returnString = f"----------------\n{self.name}\n-----------------\n        {self.description}\n"
        returnString += f"\n Current Exits:[{self.getRoomExitString()}]\n"
        returnString += f"\n Current Items in Room:{self.items}\n"

        return returnString
