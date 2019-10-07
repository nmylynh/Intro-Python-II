# Intro to Python IV w/ Beej Jorgensen

## Spec: write a program that holds product and department information about a store. User should be able to enter a department number and get a list of products in that department

### Product info is

    * quantity, iny
    * price
    * dept
    *name, string

You'll get product list later.

### Department info

    *number, int
    *name, string

### Questions

* How many products?
Under 1,000,000

* How to present data
Standard output

* How many customers?
Under 100 requests per second.

```python
class TodoList:
    def __init__(self, name):
        self.name = name
        self.item = []
    def __str__(self):
        return f"{self.name}: {Self.items}"
    def __repr__(self):
        return f"TodoList({repr(Self.name)})"

quit = False

all_lists = []

current_list = None

while not quit:

    command = input("\n(C)reate new list\n(S)elect a list ({current_list})\n(A)dd item\n(Q)uit\nCommand: ")
    # strips the leading && trailing white spaces
    command = command.lower().strip()[0] # normalize input

    if command == '':
        continue

    command = command[0]

    if command == 'q': # quit
        quit = True
    elif command == 'c': # create
        name = input("Enter list name: ").strip()

        new_list = TodoList(name)
        all_lists.append(new_list)

        print(all_lists)
    elif command == 's': # select
        name = input("Enter list name: ").strip()

        named_list = None

        for l in all_lists:
            if l.name == name:
                named_list = l
                break # get out of for loop
        if named_list is None:
            print(f"No such list named {name}")
        else:
            current_list = named_list
    elif command == 'a': # add
        if current_list is None:
            print("\n** No list selected!")
        else:
            item_name = input("Enter item: ").strip()
            current_list.items.append(item_name)

# tl = TodoList("list 1")

# tl.items.append("Get milk")
# tl.items.append("Go mountain biking")
# print(tl)
```

### Notes on code

>The is checks if both the variables point to the same object whereas the == sign checks if the values for the two variables are the same. So if the is operator returns True then the equality is definitely True, but the opposite may or may not be True.

In python, things objs, dicts, lists, these references gets passed around. You're referencing the values. Same in adventure game-- you're not assigning new values but just referencing the pointed values.

## Inheritance in OOP

```python
class Animal: # Base class; the class where we derive our subclass from
    def __init__(self, name):
        self.name = name

    def call(self):
        print(f"{self.name}: Generic animal sound")

class Vertebrate(Animal): # vertebrate is an Animal, "is-a" relationship

    def call(self): # override the parent class's call method
        print(f"{self.name}: Generic vertebrate sound")

class Mammal(Vertebrate):
    pass

class Cat(Mammal):
    def __init__(self, name, evil):
        super().__init__(name)
        self.evil = evil
    def call(self): #override the parent's class's call method
        print(f'{self.name} ({"evil" if self.evil else "not evil"}): Meow')

class Invertebrate(Animal): # invertebrate is an Animal, "is-a" relationship
    pass

animals = [
    Animal("animal 1"),
    Vertebrate("ver 1"),
    Invertebrate("invert 1"),
    Cat("cat 1),
]

for a in animals:
    a.call()
a = Animal()

v = Vertebrate()
v.call()

iv = Invertebrate()
iv.call()
```
