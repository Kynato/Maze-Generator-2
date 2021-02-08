import random as rd

class Direction:
    def __init__(self, _name):
        self.name = _name
        self.blocked = True

    def Block(self):
        self.blocked = True

    def Free(self):
        self.blocked = False

    def SwitchState(self):
        self.blocked = not bool(self.blocked)

    def IsBlocked(self):
        return self.blocked

    def GetName(self):
        return self.name
    
    def __repr__(self):
        if (self.blocked):
            return '#'
        else:
            return ' '

    def __str__(self):
        if (self.blocked):
            return '#'
        else:
            return ' '

    



class Cell:
    def __init__(self):
        self.bedrock = False #name originates from minecraft
        self.options = ['up', 'down', 'left', 'right']
        self.visited = False
        self.walls = {
        'up': Direction('up'), 
        'down': Direction('down'), 
        'left': Direction('left'), 
        'right': Direction('right')
        }

    def PickDirection(self):
        pick = rd.choice(self.options)
        self.visited = True

        return pick

    def PopDirection(self, dir):
        self.options.remove(dir)
        del self.walls[dir]

    def IsBedrock(self):
        if (self.bedrock):
            return True
        else:
            return False

    def Print(self):
        if 'up' in self.walls:
            print("###")
        else:
            print("# #")

        if 'left' in self.walls:
            print("# ", end='')
        else:
            print("  ", end='')

        if 'right' in self.walls:
            print("#")
        else:
            print(" ")

        if 'down' in self.walls:
            print("###")
        else:
            print("# #")

    def BlockingWalls(self):
        return len(self.walls)
