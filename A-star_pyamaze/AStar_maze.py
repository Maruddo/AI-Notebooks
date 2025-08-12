import pyamaze as maze
from queue import PriorityQueue
import time

# Manhattan distance heuristic
def distance(cell1, cell2):
    distancia = abs(cell1[0]-cell2[0]) + abs(cell1[1]-cell2[1])
    return distancia

# A* algorithm implementation
def aStar(m):
    start = (m.rows,m.cols)     # Start at the bottom-right corner
    end = (1,1)                 # End at the top-left corner
    g_score = {cell:float('inf') for cell in m.grid}    # Cost from start to each cell
    g_score[start] = 0
    f_score={cell:float('inf') for cell in m.grid}      # Estimated total cost (g + heuristic)
    f_score[start]=distance(start,end)
    
    pq = PriorityQueue()        # Priority queue to select the next cell with lowest f_score
    pq.put((f_score[start],distance(start,end),start)) # (f_score, heuristic, cell)
    path = {}                   # Dictionary to reconstruct the path

    while not pq.empty():
        current_cell = pq.get()[2]  # Get the cell with the lowest f_score
        if current_cell == end:
            break                   # End loop when reached the goal

        # Explore neighbors
        for direction in "NEWS": 
            if m.maze_map[current_cell][direction] == 1:    # Check if the direction is valid (not a wall)
                
                if direction == "N":
                    next_cell = (current_cell[0] - 1, current_cell[1])

                elif direction == "E":
                    next_cell = (current_cell[0], current_cell[1] + 1)

                elif direction == "W":
                    next_cell = (current_cell[0], current_cell[1] - 1)

                else:
                    next_cell = (current_cell[0] + 1, current_cell[1])
                
                # Temp costs
                temp_g_score = g_score[current_cell] + 1
                temp_f_score = temp_g_score + distance(next_cell, end)
                
                if next_cell in m.grid:
                    if temp_g_score < g_score[next_cell]:   # if the new path is better update scores
                        g_score[next_cell] = temp_g_score
                        f_score[next_cell] = temp_f_score
                        pq.put((f_score[next_cell], distance(next_cell,end), next_cell))    # Put the most promising cell next in queue
                        path[next_cell] = current_cell

    # Reconstruct the path
    forwardPath = {}
    cell=end
    while cell!=start:
        forwardPath[path[cell]] = cell
        cell=path[cell]
    return forwardPath

# Maze setup and execution
ROWS = 40
COLS = 40
m=maze.maze(ROWS,COLS)  # Create a maze object
m.CreateMaze()          # Generate the maze

pre_Astar = time.time()
path = aStar(m)                 # Run A* algorithm
post_Astar = time.time()
print(post_Astar - pre_Astar)   # Print execution time

a=maze.agent(m,footprints=True) # Create an agent to visualize the path
print(path)
m.tracePath({a:path},delay=50)  # Trace the path found by A*
m.run()