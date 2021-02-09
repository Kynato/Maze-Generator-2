from maze_cell import *
from collections import deque

class Point:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def Travel(self, dir):
        if dir == 'up':
            return Point(self.col, self.row-1)
        elif dir == 'down':
            return Point(self.col, self.row+1)
        elif dir == 'right':
            return Point(self.col+1, self.row)
        elif dir == 'left':
            return Point(self.col-1, self.row)
        else:
            print('Point travel exploded. Please check that.')

    def GetVector(self, scale, offset):
        return (self.col * scale + offset, self.row * scale + offset)

def OpositeDir(dir):
    if dir == 'up':
        return 'down'
    elif dir == 'down':
        return 'up'
    elif dir == 'right':
        return 'left'
    elif dir == 'left':
        return 'right'



class Maze:

    def __init__(self, horizontal_cells, vertical_cells, start:Point = None, finish:Point=None):
        # variables
        self.h_cells = horizontal_cells
        self.v_cells = vertical_cells
        self.table = []
        self.stack = deque()
        self.starting_point = Point(1,1)
        if start!=None:
            self.starting_point = start
        self.finishing_point = Point(vertical_cells-2,horizontal_cells-2)
        if finish!=None:
            self.finishing_point = finish

        self.path = deque()
        self.path_found = False

        self.stack.append(self.starting_point)
        self.path.append(self.starting_point)
        
        # create table of cells
        for i in range(vertical_cells):
            row = []
            for j in range(horizontal_cells):
                row.append( Cell() )

            self.table.append(row)

        # mark bedrock aka edge blocks
        for col in range(horizontal_cells):
            self.table[0][col].bedrock = True
            self.table[vertical_cells-1][col].bedrock = True

            self.table[0][col].visited = True
            self.table[vertical_cells-1][col].visited = True

        for row in range(vertical_cells):
            self.table[row][0].bedrock = True
            self.table[row][horizontal_cells-1].bedrock = True
            self.table[row][0].visited = True
            self.table[row][horizontal_cells-1].visited = True
        
        '''
        # print walls
        for i in range(vertical_cells):
            for j in range(horizontal_cells):
                if(self.table[i][j].IsBedrock()):
                    print('#', end='')
                else:
                    print(self.table[i][j].BlockingWalls(), end='')
            print('')
        '''

    def VisitedNeighbours(self, row, col):
        counter = 0
        if self.table[row-1][col].visited:
            counter += 1
        if self.table[row+1][col].visited:
            counter += 1
        if self.table[row][col-1].visited:
            counter += 1
        if self.table[row][col+1].visited:
            counter += 1

        return counter

    def FinishedGenerating(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    # This will break the walls in the freshly created maze
    def BreakWalls(self):
        top = self.stack[-1]

        if self.path_found == False:
            self.path = deque(self.stack)

        if top.row == self.finishing_point.row and top.col == self.finishing_point.col:
            self.path_found = True
            # copy by value, not by reference
            self.path = deque(self.stack)

        self.table[top.row][top.col].visited = True
        c = self.table[top.row][top.col]

        #delete this?
        if c.IsBedrock():
            print('Cell is bedrock. This shouldnt happen.')

        if self.VisitedNeighbours(top.row, top.col) > 3:
            #print('popping ' + str(top.row) + ', ' + str(top.col))
            self.stack.pop()
            return
            
        pick = c.PickDirection()
        #print(pick)

        if pick == 'up':
            next_c = self.table[top.row-1][top.col]
        elif pick == 'down':
            next_c = self.table[top.row+1][top.col]
        elif pick == 'right':
            next_c = self.table[top.row][top.col+1]
        elif pick == 'left':
            next_c = self.table[top.row][top.col-1]

        if not next_c.IsBedrock() and not next_c.visited:
            self.stack.append(top.Travel(pick))
            c.PopDirection(pick)
            next_c.PopDirection(OpositeDir(pick))
        


        


        
        





