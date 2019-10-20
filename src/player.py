# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = Inventory()

    def __str__(self):
        return f'Player name: {self.name}, Current_room: {self.current_room}'
    
    def actions(self, action):
        if action == 'n':
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
        elif action == 's':
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
        elif action == 'e':
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
        elif action == 'w':
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
        elif action == 'i':
            self.inventory.show_inventory()
        elif action == 'f':
            if self.current_room.items:
                self.current_room.room_items()
                item = input('What would you like to pick up?\n')
                if self.current_room.items[item]:
                    self.inventory.add_to_inventory(item, self.current_room.items[item].pop())
                else:
                    print(f'Are you sure there is a(n) {item} here? \n You should check the room again.\n')
            else: 
                print('There are no items in this room.\n')
        elif action != 'n' or action != 's' or action != 'e' or action != 'w' or action != 'i' or action != 'f' or action !='q':
            print('Invalid action.\n')
        elif action == 'q':
            print('Goodbye.')
        else:
            print('You cannot go there.\n\n')
               
class Inventory:
    def __init__(self):
        self.items = {}
    
    def show_inventory(self):
        if self.items is not None:
            print(f'There are {len(self.items)} item(s) in your inventory.\n')
            for name, description in self.items.items():
                print(f'{name}: {description}')
        else:
            print('There are no items in your inventory.')
    
    def add_to_inventory(self, item, description):
        self.items[item] = description
        


# user = Player('Jim', 'Foyer',  items={'candle': 'it lights up stuff', 'sword': 'it chops up stuff'})
# print(user.items)

# print(user)


# print(user.inventory.show_inventory())




