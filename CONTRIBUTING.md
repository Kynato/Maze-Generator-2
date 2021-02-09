Hi! Glad to see you here :)

In case you want to contribute here is the TODO list:
  - Maze conversion from table[][] to graph
  
        This will enable easier implementation of pathfinding agorithms like Dijkstra or A*
      
  - Wall rendering optimization.
  
        Now every single wall is drawn alone, one by one causing performace problems in case of bigger mazes.
        Would be faster to draw them all at once.
      
  - Maze output to .TXT or other formats
  
        So it can be used in other projects
        Split each maze_cell to 3x3 ASCII:
      
          wall -> '#'
          space -> ' '
        
  - Printable maze
  
        Conversion to .PDF
    
  - Interactivity?
  
        Playable character?
  
  - Conversion to 3D model
    
        Blender extension?
        Minecraft object?
        
  - Bulletproof code
  
        Reinforce the code with try catch and some smart ifs
        
  - Your ideas?
      
        Feel free to implement and PULL REQUEST.
