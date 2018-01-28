"""Insantiate Items"""

class Item(object):
    """Define basic Item"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def info(self):
        """Return Item info"""
        return "{}\n=====\n{}".format(self.name, self.description)

class Pack(Item):
    """Define Pack"""
    def __init__(self):
        self.inventory = []
        super().__init__(name=Pack, description="A spacious leather bag")

    def stash(self):
        """Print iventory"""
        return "Inventory: {}".format(str(self.inventory))

class Orb(Item):
    """Define Orbs"""
    def __init__(self, color):
        self.color = color
        super().__init__(self, self.name, self.desc)

twizzlers = Item("twizzlers", "The tastiest of tasty snacks!")
blue_orb = Orb("blue", "blue orb", "A glowing %" % self.name)
green_orb = Orb("green", "green orb", "A glowing %" % self.name)
purple_orb = Orb("purple", "purple orb", "A glowing %" % self.name)
red_orb = Orb("red", "red orb", "A glowaing %" % self.name)
yellow_orb = Orb("yellow", "yellow orb", "A glowing %" % self.name)
orange_orb = Orb("orange", "orange orb", "A glowing %" % self.name)
white_orb = Orb("white", "white orb","A glowing %" % self.name)
black_orb = Orb("black", "black orb","A glowing %" % self.name)
