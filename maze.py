from maze_cell import *

class Maze:

    def __init__(self, horizontal_cells, vertical_cells):
        # variables
        self.h_cells = horizontal_cells
        self.v_cells = vertical_cells
        self.table = []
        
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

        for row in range(vertical_cells):
            self.table[row][0].bedrock = True
            self.table[row][horizontal_cells-1].bedrock = True
        
        # print walls
        for i in range(vertical_cells):
            for j in range(horizontal_cells):
                if(self.table[i][j].IsBedrock()):
                    print('#', end='')
                else:
                    print(self.table[i][j].BlockingWalls(), end='')
            print('')

        


        
        





