"""Create a callable map to display current location and explored rooms.

Classes:
    MiniMap(object): Establish the map.
Attributes:
    TSIZE (int): The size of a tile.
    HALF (int): Half of TSIZE
    RECT: Condensed pygame function for drawing rectangles.
    CIRCLE: Condensed pygame function for drawing circles.

    WHITE (tuple): RGB white:
    BLUE (tuple): RGB blue:
    GREEN (tuple): RGB green.
    PURPLE (tuple): RGB purple.
    RED (tuple): RGB red.
    YELLOW (tuple): RGB yellow.
    ORANGE (tuple): RGB orange.
    BLACK (tuple): RGB black.
    GRAY (tuple): RGB gray.

    RM_COORDS (dict): Room coordinates (-x and -y values).
"""
import pygame

# Useful constants.
TSIZE = 60
HALF = int(TSIZE / 2)
RECT = pygame.draw.rect
CIRCLE = pygame.draw.circle

# Colors.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (60, 255, 0)
PURPLE = (165, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Room coordinates.
COORDS = {
    1: {"x": TSIZE * 3, "y": TSIZE * 6},
    2: {"x": TSIZE * 3, "y": TSIZE * 4},
    3: {"x": TSIZE * 5, "y": TSIZE * 4},
    4: {"x": TSIZE, "y": TSIZE * 4},
    5: {"x": TSIZE, "y": TSIZE * 2},
    6: {"x": TSIZE * 5, "y": TSIZE * 2},
    7: {"x": TSIZE * 3, "y": TSIZE * 2},
    8: {"x": TSIZE * 3, "y": 10}
}

# Room data passed to RECT
RM_DATA = {
    1: (COORDS[1]["x"], COORDS[1]["y"], TSIZE, TSIZE),
    2: (COORDS[2]["x"], COORDS[2]["y"], TSIZE, TSIZE),
    3: (COORDS[3]["x"], COORDS[3]["y"], TSIZE, TSIZE),
    4: (COORDS[4]["x"], COORDS[4]["y"], TSIZE, TSIZE),
    5: (COORDS[5]["x"], COORDS[5]["y"], TSIZE, TSIZE),
    6: (COORDS[6]["x"], COORDS[6]["y"], TSIZE, TSIZE),
    7: (COORDS[7]["x"], COORDS[7]["y"], TSIZE, TSIZE),
    8: (COORDS[8]["x"], COORDS[8]["y"], TSIZE, TSIZE),
}

# Set FPS object
FPS = pygame.time.Clock()


class MiniMap(object):
    """Show a map of explored rooms.

    Attributes:
        WIDTH: Map width in tiles.
        HEIGHT: Map height in tiles.
        MDWIDTH: Map width in pixels.
        MHEIGHT: Map height in pixels.
    Public Methods:
        start()
        render()
        run()
    """

    def __init__(self, width: int, height: int) -> None:
        """Initialize necessary pygame modules to speed up map rendering."""
        self.WIDTH = width
        self.HEIGHT = height
        self.MWIDTH = TSIZE * self.WIDTH
        self.MHEIGHT = TSIZE * self.HEIGHT

        pygame.__init__("display")
        pygame.__init__("event")
        pygame.__init__("draw")

    def render(self, num: int, room: int) -> None:
        """Render the map.

        Args:
            num: The number of ROOMS to blit.
            room: The current room of the Player.
        """
        pygame.font.init()

        # Store RECT data as a string for later eval.
        ROOMS = [
            "RECT(DSPLY, WHITE, RM_DATA[1], 1)",
            "RECT(DSPLY, BLUE, RM_DATA[2], 1)",
            "RECT(DSPLY, GREEN, RM_DATA[3], 1)",
            "RECT(DSPLY, PURPLE, RM_DATA[4], 1)",
            "RECT(DSPLY, RED, RM_DATA[5], 1)",
            "RECT(DSPLY, YELLOW, RM_DATA[6], 1)",
            "RECT(DSPLY, ORANGE, RM_DATA[7], 1)",
            "RECT(DSPLY, GRAY, RM_DATA[8], 1)"
        ]
        DSPLY = pygame.display.set_mode((self.MWIDTH + 10, self.MHEIGHT + 40))
        FONT = pygame.font.Font(None, 18)
        text = FONT.render("Press [Q] to return.", True, WHITE, BLACK)
        # Player coordinates.
        pos_x = int(COORDS[room]["x"] + HALF)
        pos_y = COORDS[room]["y"] + HALF
        # Player indicator.
        pos_indi = CIRCLE(DSPLY, WHITE, (pos_x, pos_y), 5)

        pygame.display.set_caption("The C R A V I N G")
        # Render background.
        DSPLY.fill(BLACK)
        # Render text.
        DSPLY.blit(text, (TSIZE * 3 - 25, self.MHEIGHT + 20))
        # Render the necessary ROOMS.
        for x in range(0, num + 1):
            eval(ROOMS[x])
        # TODO Add a color shifting glow to the POS indicator.
        # Emphasize Player indicator with a bounce animation.
        # BUG bounce animation is not rendering properly inside render()
        # BUG may need to move bounce animation back to run()
        # for x in range(10):
        #     FPS.tick(30)
        #     DSPLY.fill(BLACK, pos_indi)
        #     pos_y -= 1
        #     CIRCLE(DSPLY, WHITE, (pos_x, pos_y), 5)
        #     pygame.display.update()
        # for x in range(10):
        #     FPS.tick(30)
        #     DSPLY.fill(BLACK, pos_indi)
        #     pos_y += 1
        #     CIRCLE(DSPLY, WHITE, (pos_x, pos_y), 5)
        #     pygame.display.update()

    def run(self, rooms: int=0, current: int=1) -> None:
        """Main method of MiniMap(): render all graphics and handle events.

        Args:
            rooms: The number of discovered rooms to render (default=0).
            current: The current room (default=1).
        """
        while True:
            # TODO Implement player POS attributes from Player.py
            self.render(rooms, 1)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return False  # THIS LINE IS CRUCIAL
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    return False  # THIS LINE IS CRUCIAL
            pygame.display.flip()


# For testing purposes
test = MiniMap(7, 7)
test.run()
