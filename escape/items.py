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
        super().__init__(name="Pack", description="a spacious leather bag", origin=1)
        self.pocket = []

    def contents(self):
        """Print iventory"""
        if self.pocket == []:
            return "Your pack is empty!"
        return "Inventory: {}".format(str(self.pocket))

class Orb(Item):
    """Define Orbs"""
    def __init__(self, name, description, origin, color):
        super().__init__(name, description, origin)
        self.color = color

    def rezonate(self):
        """Rezonate Orb with Door"""
        return "a pulsating {} light shines from within the orb.".format(self.color)

PACK = Pack()
TWIZZLERS = Item("Twizzlers", "the tastiest of tasty snacks!", 8)
BLUE_ORB = Orb("Blue Orb", "a glowing blue orb", 1, "blue")
GREEN_ORB = Orb("Green Orb", "a glowing green orb", 2, "green")
PURPLE_ORB = Orb("Purple Orb", "a glowing purple orb", 3, "purple")
RED_ORB = Orb("Red Orb", "a glowing red orb", 4, "red")
YELLOW_ORB = Orb("Yellow Orb", "a glowing yellow orb", 5, "yellow")
ORANGE_ORB = Orb("Orange Orb", "a glowing orange orb", 6, "orange")
WHITE_ORB = Orb("White Orb", "a glowing white orb", 7, "white")
BLACK_ORB = Orb("Black Orb", "a glowing black orb", 0, "black")
