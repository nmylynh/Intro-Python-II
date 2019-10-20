# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'Player name: {self.name}, Current_room: {self.current_room}, Items: {self.items}'
    
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
            Inventory.show_inventory(self)
            

class Inventory(Player):
    def __init__(self, items):
        super().__init__(items)
    
    def show_inventory(self):
        if self.items is not None:
            print(f'There are {len(self.items)} in your inventory.\n')
            for name, description in self.items:
                print(f'{name}: {description}')
        else:
            print('There are no items in your inventory.')
        


user = Player('Jim', 'Foyer',  items={'candle': 'it lights up stuff', 'sword': 'it chops up stuff'})
print(user.items)

print(user)
user_inventory = Inventory(items=user.items)

print(user_inventory.show_inventory())




