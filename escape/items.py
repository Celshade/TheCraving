"""Module: Define Items"""

class Item(object):
    """Define basic Item"""
    def __init__(self, name, description, origin):
        self.name = name
        self.description = description
        self.origin = origin

    def __str__(self):
        """Return Item name"""
        return self.name

    def info(self):
        """Return full Item description"""
        return "**{}**\n{}".format(self.name, self.description)

    def origin_id(self):
        """Returns ROOM origin"""
        return self.origin

class Pack(Item):
    """Define Pack"""
    def __init__(self):
        super().__init__(name="Pack", description="A spacious leather bag", origin=1)
        self.inventory = []

    def contents(self):
        """Print iventory"""
        if self.inventory == []:
            return "The pack is empty!"
        return "Inventory: {}".format(self.inventory)

class Orb(Item):
    """Define Orbs"""
    def __init__(self, name, description, origin, color,):
        super().__init__(name, description, origin)
        self.color = color

    def rezonate(self):
        """Rezonate Orb with Door"""
        return "A pulsating {} light shines from within the orb.".format(self.color)

PACK = Pack()
TWIZZLERS = Item("Twizzlers", "The tastiest of tasty snacks!", 8)
BLUE_ORB = Orb("Blue Orb", "A glowing blue orb", 1, "blue")
GREEN_ORB = Orb("Green Orb", "A glowing green orb", 2, "green")
PURPLE_ORB = Orb("Purple Orb", "A glowing purple orb", 3, "purple")
RED_ORB = Orb("Red Orb", "A glowaing red orb", 4, "red")
YELLOW_ORB = Orb("Yellow Orb", "A glowing yellow orb", 5, "yellow")
ORANGE_ORB = Orb("Orange Orb", "A glowing orange orb", 6, "orange")
WHITE_ORB = Orb("White Orb", "A glowing white orb", 7, "white")
BLACK_ORB = Orb("Black Orb", "A glowing black orb", 0, "black")
