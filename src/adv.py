from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items={'torch': 'Found convieniently placed on the entrance of the cave.'}),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items={'journal': 'It is found in a rusty desk in the foyer. It seems to be the journal of someone who used to mine here.'}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items={'sword': 'A sword found on a cliff from the Grand Overlook. Dusty, but still sharp, it seems to be engraved but you cannot seem to read the language.', 'rope': 'It seems like someone tried use this to climb down the cliff at the Grand Overlook.'}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items={'shoe': 'An old shoe overturned in some dirt of the narrow passage. Maybe it was dropped in haste.'} ),

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

print('WELCOME! Your super cool adventure...starts...now!!\n')

player = Player(input("Please enter your character name: "), room['outside'])

print(f'Your current location is the {player.current_room.name} room. {player.current_room.description}.\n')

action = input("What would you like to do? \n Move: North(n), South(s), East(e), or West(w) \n Open Inventory(i) \n Search for items(f) \n Quit Game(q)\n\n")

player.actions(action)

while True:
    if action == 'q':
        break
    elif player.current_room is None:
        break
    else:
        print(f'Your current location is the {player.current_room.name} room. {player.current_room.description}.\n\n')
        action = input("What would you like to do? \n Move: North(n), South(s), East(e), or West(w) \n Open Inventory(i) \n Search for items(f) \n Quit Game(q)\n\n")
        player.actions(action)
        continue
