from room import Room
from player import Player
import textwrap
# Declare all the rooms whoo
# remember, you defined Room as first having a name, which for Outside would be "Outside Cave Entrance", and then there is a description.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mountain beckons"),

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

print("Welcome to the Treasure Hunt, a game designed by tryingtokeepup. I hope you can, *snicker, ... keep up. Oh my I chottle myself unduly, yes.")

# gamplay loop
while True:
    # First, let's ask the player what their name is, and then store that, along with the current_room, outside, inside a new instance of Player
    player_name = input('Hello traveler, what is your name? : ')
    player = Player(player_name, room['outside'])
    print(
        f'Gotcha! So, your name is {player.name}. You are currently {player.current_room.name}')
