# IMPORTS
from gui_fx import *
from maze import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 900
WINDOW_WIDTH = WINDOW_HEIGHT
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)

# SIZE OF THE MAZE
maze_size = 10
m = Maze(maze_size, maze_size, Point(1, 1))
#m = Maze(1500, 1000, Point(1, 1))

# Draw instantly
'''
while(not m.FinishedGenerating()):
   m.BreakWalls()

gui.DrawMaze(m)
gui.DrawPath(m)
'''



while 1:
   for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()

   # Animate
   if not m.FinishedGenerating():
      m.BreakWalls()
      gui.DrawMaze(m)
      gui.DrawPath(m)

   pygame.time.wait(100)
   pygame.display.flip()