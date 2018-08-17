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

# Colors.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (60, 255, 0)
PURPLE = (165, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)


class MiniMap(object):
    """Show a map of explored rooms.

    Attributes:
        TSIZE: Tile size in pixels.
        WIDTH: Map width in tiles.
        HEIGHT: Map height in tiles.
        MDWIDTH: Map width in pixels.
        MHEIGHT: Map height in pixels.
    Public Methods:
        start()
        render()
        run()
    """

    def __init__(self, tilesize: int, width: int, height: int) -> None:
        """Initialize necessary pygame modules to speed up map rendering."""
        self.TSIZE = tilesize
        self.WIDTH = width
        self.HEIGHT = height
        self.MWIDTH = self.TSIZE * self.WIDTH
        self.MHEIGHT = self.TSIZE * self.HEIGHT

        pygame.__init__("display")
        pygame.__init__("event")
        pygame.__init__("draw")
        pygame.font.init()

    def render(self, num: int=1) -> None:
        """Render the map.

        Args:
            num: The number of rooms to render (default=1).
        """
        # Ignore flake8 error
        RECT = pygame.draw.rect
        # Store RECT data as a string for later eval.
        ROOMS = [
            "RECT(DSPLY, WHITE, (self.TSIZE * 3, self.TSIZE * 6, 60, 60), 1)",
            "RECT(DSPLY, WHITE, (self.TSIZE * 3, self.TSIZE * 6, 60, 60), 1)",
            "RECT(DSPLY, BLUE, (self.TSIZE * 3, self.TSIZE * 4, 60, 60), 1)",
            "RECT(DSPLY, PURPLE, (self.TSIZE, self.TSIZE * 4, 60, 60), 1)",
            "RECT(DSPLY, GREEN, (self.TSIZE * 5, self.TSIZE * 4, 60, 60), 1)",
            "RECT(DSPLY, RED, (self.TSIZE, self.TSIZE * 2, 60, 60), 1)",
            "RECT(DSPLY, YELLOW, (self.TSIZE * 5, self.TSIZE * 2, 60, 60), 1)",
            "RECT(DSPLY, ORANGE, (self.TSIZE * 3, self.TSIZE * 2, 60, 60), 1)",
            "RECT(DSPLY, GRAY, (self.TSIZE * 3, 10, 60, 60), 1)"
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
        DSPLY.blit(text, (self.TSIZE * 3 - 25, self.MHEIGHT + 20))

    def run(self) -> None:
        """Call self.render(), update DSPLY, and close pygame when done."""
        while True:
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return False  # THIS LINE IS CRUCIAL
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    return False  # THIS LINE IS CRUCIAL
            pygame.display.flip()


# TODO clean up hard-code
# For testing purposes
test = MiniMap(60, 7, 7)
test.run()
