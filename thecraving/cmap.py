"""Create a callable map to display current location and explored rooms.

Classes:
    MiniMap(): Establish the map.
Attributes:
    WHITE: RGB white:
    BLUE: RGB blue:
    GREEN: RGB green.
    PURPLE: RGB purple.
    RED: RGB red.
    YELLOW: RGB yellow.
    ORANGE: RGB orange.
    BLACK: RGB black.
    GRAY: RGB gray.
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
WHITE_X, WHITE_Y = TSIZE * 3, TSIZE * 6
BLUE_X, BLUE_Y = TSIZE * 3, TSIZE * 4
GREEN_X, GREEN_Y = TSIZE * 5, TSIZE * 4
PURPLE_X, PURPLE_Y = TSIZE, TSIZE * 4
RED_X, RED_Y = TSIZE, TSIZE * 2
YELLOW_X, YELLOW_Y = TSIZE * 5, TSIZE * 2
ORANGE_X, ORANGE_Y = TSIZE * 3, TSIZE * 2
GRAY_X, GRAY_Y = TSIZE * 3, 10

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
        # Player coordinates.
        # TODO Change coordinates as Player navigates the rooms.
        self._x = WHITE_X + HALF
        self._y = WHITE_Y + HALF

        pygame.__init__("display")
        pygame.__init__("event")
        pygame.__init__("draw")

    def render(self, num: int) -> None:
        """Render the map.

        Args:
            num: The number of ROOMS to blit.
        """
        pygame.font.init()

        # Store RECT data as a string for later eval.
        ROOMS = [
            "RECT(DSPLY, WHITE, (WHITE_X, WHITE_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, BLUE, (BLUE_X, BLUE_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, GREEN, (GREEN_X, GREEN_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, PURPLE, (PURPLE_X, PURPLE_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, RED, (RED_X, RED_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, YELLOW, (YELLOW_X, YELLOW_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, ORANGE, (ORANGE_X, ORANGE_Y, TSIZE, TSIZE), 1)",
            "RECT(DSPLY, GRAY, (GRAY_X, GRAY_Y, TSIZE, TSIZE), 1)"
        ]
        DSPLY = pygame.display.set_mode((self.MWIDTH + 10, self.MHEIGHT + 40))
        FONT = pygame.font.Font(None, 18)
        text = FONT.render("Press [Q] to return.", True, WHITE, BLACK)

        pygame.display.set_caption("The C R A V I N G")
        # Render background.
        DSPLY.fill(BLACK)
        # Render the necessary ROOMS.
        for x in range(0, num + 1):
            eval(ROOMS[x])
        # Render text.
        DSPLY.blit(text, (TSIZE * 3 - 25, self.MHEIGHT + 20))
        # Player POS indicator.
        CIRCLE(DSPLY, WHITE, (self._x, self._y), 5)
        # TODO Add a color shifting glow to the POS indicator.

    def run(self, rooms: int=0) -> None:
        """Call self.render(), update DSPLY, and close pygame when done.

        Args:
            rooms: The number of rooms to pass to render() (default=0).
        """
        while True:
            self.render(rooms)
            pygame.display.flip()
            # TODO Condense player indicator movement into a function
            # Bounce the player indicator up.
            for x in range(20):
                FPS.tick(65)
                self._y -= 1
                self.render(rooms)
                pygame.display.flip()
            # Bounce the player indicator down.
            for x in range(20):
                FPS.tick(60)
                self._y += 1
                self.render(rooms)
                pygame.display.flip()

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
# test = MiniMap(7, 7)
# test.run()

# TODO clean up hard-code
# TODO clean up render()
