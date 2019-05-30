from room import Room
from player import Player
from item import Item
from colorama import Fore, Back, Style
import textwrap
import os
# Eileen's Birthday Adventure
# Eileen needs to find all her pals and cool dudes and gamer ladies, and have an awesome birthday bash.
# Overall goal is to reach the quarentine room, and free Nedim.
# We have to collect Bondor, and Laryna and Carlo, and Kai
# Declare all the rooms whoo
# remember, you defined Room as first having a name, which for Outside would be "Outside Cave Entrance", and then there is a description.
room = {
    'outside':  Room("Terria Fandango",
                     """North of you, Nedim's quarentine towers over you. Only then will Eileen's birthday bash be complete and fufilling."""),

    'foyer':    Room("Fancy Hallway", """Light noise filters through the door behind you, until it closes onimously with a clank. You spot in front of you a clearing that seems to jut over a endless expanse. To the east of you, there is a narrow pathway to some silky darkness."""),

    'overlook': Room("Grand Overlook", """You look down, and you instantly regret doing so. There seems to be glistening objects somewhere far below you, but you don't think that Nedim is waiting for you down there. However, a wild Bondor appears, and jumps on your back. You are stuck with him for now."""),

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
bondor = Item("Mini Bondor",
              "Bondor has jumped on you back, but quickly tires of it and hops into your backpack.")
room['outside'].items.append(rock)

items = [rock, cookie]
items_names = [item.name for item in items]


item_to_find_name = "Rock"
# should put this into the item.py class, will refactor
for i in range(len(items)):
    if items[i].name.lower() == item_to_find_name.lower():
        item = items.pop(i)
        break

print(item.name)

#######################################################

############### Main Game Loop #######################
valid_directions = ['n', 's', 'e', 'w']
take = 't'
drop = 'd'
print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)
print(Fore.YELLOW + Back.BLACK + "Welcome to the Treasure Hunt, \n a game designed by tryingtokeepup. \nI hope you can, *snicker, ... keep up. Oh my I chottle myself unduly, yes.")

print(Fore.BLUE + '====================================\n' + Style.RESET_ALL)

player_name = input(Fore.YELLOW + Back.BLACK +
                    'Hello traveler, what is your name? : \n')
# let's start everyone off at the outside room.
current_room = room['outside']
# let's ask the player what their name is, and then store that, along with the current_room, outside, inside a new instance of Player
player = Player(player_name, current_room)

print(
    f"Gotcha! So, your name is {player.name}. You are currently {player.current_room.name}. \n")

print(f"{player.current_room}")
# while True:
#     cmd = input("-->")
#     if cmd in valid_directions:
#         current_room = player.current_room
#         player.travel(cmd)
#     elif cmd == take:
#         # this is fine. everything is on fire but life is fine
#         # i am not currently pancaking help me i dont actually know how to program
#         player.get_item(player.current_room.items[0])
#     elif cmd == drop:
#         player.current_room.add_item(player.items[0])

#     elif cmd == "q":
#         print('Ahhh man, alright. See you in the next world.')
#         break
#     else:
#         print('Didn\'t catch that. Try again?')

# gamplay loop

while True:

    cmd = input(
        "Alright, so ... make a move. Input a cardinal direction please. \n")

    if cmd == "i":
        print("\n To go north, enter n. \n To go east, enter e.  To go south, enter s. \n To go west, enter s. \n  If you need to quit, just enter q to quit out. \n ... Yah wuss. \n")

    elif cmd in ["n", "s", "e", "w"]:
        player.travel(cmd)
    elif cmd == "q":
        print('Ahhh man, alright. See you in the next world.')
        break
# quick commit
