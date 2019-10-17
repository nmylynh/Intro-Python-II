# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        if items is None:
            self.items= {}
        else:
            self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        return {'name': self.name, 'description': self.description, 'items': self.items}


        Room('Kitchen', 'You make food here', Item('candle', 'it lights up shit'))


class Item:
    def