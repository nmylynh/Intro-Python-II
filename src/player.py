# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.inventory = Inventory(items)

    def __str__(self):
        return f'Player name: {self.name}, Current_room: {self.current_room}'
    
    def actions(self, action):
        if action == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
                print('You go north.\n')
            else:
                print('Nothing is towards the north.')
        elif action == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
                print('You go south.\n')
            else:
                print('Nothing is south.')
        elif action == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
                print('You go east.\n')
            else:
                print('Nothing is east.')
        elif action == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
                print('You go west.\n')
            else:
                print('Nothing is west.')
        elif action == 'i':
            self.inventory.show_inventory()
        elif action == 'f':
            if self.current_room.items:
                self.current_room.room_items()
                item = input('Which item would you like to pick up? (Type the item name)\n')
                item_check = self.current_room.items.get(item)
                if item_check:
                    self.inventory.add_to_inventory(item, self.current_room.items.pop(item))
                else:
                    print(f'Are you sure there is a(n) {item} here? \n You should check the room again.\n')
            else: 
                print('There are no items in this room.\n')
        elif action == 'q':
            print('Goodbye.')
        else:
            print('Invalid action.\n\n')
               
class Inventory:
    def __init__(self, items):
        if items == None:
            self.items = {}
        else: 
            self.items = items
    
    def show_inventory(self):
        if self.items is not None:
            print(f'There are {len(self.items)} item(s) in your inventory.\n')
            for name, description in self.items.items():
                print(f'{name}: {description}')
        else:
            print('There are no items in your inventory.')
    
    def add_to_inventory(self, item, description):
        self.items[item] = description
        print(f'You pick up a(n) {item}.')


# user = Player('Jim', 'Foyer', )
# print(user.items)

# print(user)


# print(user.inventory.show_inventory())




