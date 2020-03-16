import heapq
'''
bennet file bro
'''

def find_start_and_end(grid):
    s_found = False
    g_found = False
    for y in range(len(grid)):
        if s_found and g_found: # break if both start and goal points have been found
            break
        if "S" in grid[y]: # if start is in this row
            for x in range(len(grid[y])): # get the coordinates
                if grid[y][x] == "S":
                    x_start = x
                    y_start = y
                    s_found = True
                    break
        if "G" in grid[y]: # if goal is in this row
            for x in range(len(grid[y])): # get the coordinates
                if grid[y][x] == "G":
                    x_goal = x
                    y_goal = y
                    g_found = True
                    break
    if s_found and g_found:
        return (y_start, x_start), (y_goal, x_goal)
    else:
        print("start or goal not found")

def heuristic(a, b):
    # Chebyshev distance on a grid
    return max(abs(b[1] - a[1]), abs(b[0] - a[0]))

def getneighbours(graph, coord):
    neighbours = []

    for y in range(coord[0] - 1, coord[0] + 2):
        for x in range(coord[1] - 1, coord[1] + 2):
            if y in range(0, len(graph)) and x in range(0, len(graph[0])) and \
            graph[y][x] != 'X' and (y, x) != coord:
                neighbours.append((y, x))
    
    print(neighbours)
    return neighbours

def main():
    # file input
    with open("pathfinding_a.txt", 'r') as f_input:
        grid = [[x for x in line if x != "\n"] for line in f_input.readlines()]

    #
    # the grid variable is the initial state; do stuff and set the solution to grid
    # grid goes grid[row][column]
    #
    start_coords, goal_coords = find_start_and_end(grid)
    print(goal_coords)
    frontier = []
    heapq.heappush(frontier, (0, start_coords))
    came_from = {}
    cost_so_far = {}
    came_from[start_coords] = None
    cost_so_far[start_coords] = 0

    while len(frontier) > 0: 
        current = heapq.heappop(frontier)[1]
        
        if current == goal_coords:
            break

        print(current)
        for neighbour in getneighbours(grid, current): 
            new_cost = cost_so_far[current] + 1
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic(goal_coords, neighbour)
                heapq.heappush(frontier, (priority, neighbour))
                came_from[neighbour] = current

    print(came_from)
        

    # file output
    with open("pathfinding_a_out.txt", 'w') as f_output:
        output_list = []
        # convert to a 1D list of strings
        for line in grid:
            output_list.append(''.join(line) + "\n")
        # removing last "\n"
        output_list[-1] = output_list[-1][:-1]
        # writing to the file
        f_output.writelines(output_list)

if __name__ == "__main__":
    main()
