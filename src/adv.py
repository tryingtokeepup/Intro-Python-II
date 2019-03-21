from room import Room
from player import Player
from item import Item
from colorama import Fore, Back, Style
import textwrap
import os

# Declare all the rooms whoo
# remember, you defined Room as first having a name, which for Outside would be "Outside Cave Entrance", and then there is a description.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mountain beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add some items

rock = Item(
    "Rock", "This is a rock. Pointy, rough, and can be a makeshift weapon in times of need.")
cookie = Item(
    "Cookie", "Cookies are awesome. Put one in your mount and chew. It's going to be great.")

items = [rock, cookie]
items_names = [item.name for item in items]


item_to_find_name = "Rock"
# should put this into the item.py class, will refactor
for i in range(len(items)):
    if items[i].name.lower() == item_to_find_name.lower():
        item = items.pop(i)
        break

print(item.name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Let's begin the game loop!
# welcome message
valid_directions = ['n', 's', 'e', 'w']


print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)
print(Fore.YELLOW + Back.BLACK + "Welcome to the Treasure Hunt, \n a game designed by tryingtokeepup. \nI hope you can, *snicker, ... keep up. Oh my I chottle myself unduly, yes.")

print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)

player_name = input(Fore.YELLOW + Back.BLACK +
                    'Hello traveler, what is your name? : ')
# let's start everyone off at the outside room.
current_room = room['outside']
# let's ask the player what their name is, and then store that, along with the current_room, outside, inside a new instance of Player

player = Player(player_name, current_room)
print(
    f'Gotcha! So, your name is {player.name}. You are currently {player.current_room.name}')


while True:
    cmd = input("-->")
    if cmd in valid_directions:
        current_room = player.current_room
        player.travel(cmd)
    elif cmd == "q":
        print('Ahhh man, alright. See you in the next world.')
        break
    else:
        print('Didn\'t catch that. Try again?')

# gamplay loop
# while True:
#     player = Player(player_name, current_room)
#     print(
#         f'You examine the room you are in. {player.current_room.description}')
#     cmd = input(
#         "Alright, so ... make a move. \n To go north, enter n. \n To go east, enter e. \n To go south, enter s. \n To go west, enter s. \n  If you need to quit, just enter q to quit out. \n ... Yah wuss. \n")
#     if cmd == "n":

#         if current_room.n_to == None:
#             print(
#                 'You looked to the north, but you saw only darkness. Try another direction.')

#         current_room = current_room.n_to
#     elif cmd == "q":
#         print('Ahhh man, alright. See you in the next world.')
#         break
# quick commit
