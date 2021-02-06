# IMPORTS
from gui_fx import *
from maze import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)

m = Maze(30, 8)

while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()