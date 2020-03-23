import heapq
import math

'''
Class: 352
Professor: Givigi
Authors: Shreyansh Anand, Bennet Montgomery, Evelyn Yach, Daniel Oh, Spencer Dallas
Program to conduct pathfinding based on the input file provided using various heuristics.
'''


def find_start_and_end(grid):
    """
    Simple function that looks for both the S and G in the board
    :param grid: takes in the input file
    :return: returns the coordinates of the starting position and the goal
    """
    s_found = False
    g_found = False
    for y in range(len(grid)):
        if s_found and g_found:  # break if both start and goal points have been found
            break
        if "S" in grid[y]:  # if start is in this row
            for x in range(len(grid[y])):  # get the coordinates
                if grid[y][x] == "S":
                    x_start = x
                    y_start = y
                    s_found = True
                    break
        if "G" in grid[y]:  # if goal is in this row
            for x in range(len(grid[y])):  # get the coordinates
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
    """
    Uses the Chebyshev distance heuristic to identify the scores of each potential movement the agent can take
    :param a: the current location of the agent
    :param b: the potential location of the agent
    :return: the Chebyshev score
    """
    return max(abs(b[1] - a[1]), abs(b[0] - a[0]))


def getneighboursdiag(graph, coord):
    """
    Function to identify the diagonal neighbours of the current location of the agent
    :param graph: the graph to look through
    :param coord: the current location of the agent
    :return: the neighbours of the agent
    """
    neighbours = []
    # getting diagonal nehbours
    for y in range(coord[0] - 1, coord[0] + 2):
        for x in range(coord[1] - 1, coord[1] + 2):
            if y in range(0, len(graph)) and x in range(0, len(graph[0])) and graph[y][x] != 'X' and (y, x) != coord:
                neighbours.append((y, x))
    return neighbours


def getneighbours(graph, coord):
    """
    Function to identify the left, right and up and down neighbours of the agent
    :param graph: the graph to look through
    :param coord: the current location of the agent
    :return: the left-right & up-down neighboours of the agent
    """
    neighbours = []

    # getting right left neighbours
    for x in range(coord[1] - 1, coord[1] + 2):
        if x in range(0, len(graph[0])) and graph[coord[0]][x] != 'X' and (coord[0], x) != coord:
            neighbours.append((coord[0], x))

    # getting up down neighbours
    for y in range(coord[0] - 1, coord[0] + 2):
        if y in range(0, len(graph)) and graph[y][coord[1]] != 'X' and (y, coord[1]) != coord:
            neighbours.append((y, coord[1]))

    return neighbours


def clean_queue(queue, tup):
    """

    :param queue:
    :param tup:
    :return:
    """
    for i in range(0, len(queue) - 1):
        if queue[i][1] == tup:
            queue.pop(i)
            heapq.heapify(queue)

    return queue


def grid_print(grid):
    """
    A helper function to print the gird in an easy to comprehend way
    :param grid: the grid t print
    :return: nothing, as it is just printed
    """
    for line in range(len(grid)):
        print(grid[line])
    print("")


def final_grid(path, grid):
    """
    Function to  make the final grid with the path identified.
    :param path: the path the agent takes to go from the start to the goal
    :param grid: the grid that the agent is in
    :return: the actual final grid where P shows the entire path the agent took
    """
    for coords in path:
        grid[coords[0]][coords[1]] = 'P'
    return grid


def astar(grid, accept_diags):
    """
    A* Function that makes the actual path the agent takes from the starting position to the goal.
    :param grid: the grid for the agent to traverse
    :param accept_diags: Flag to see if we want to evaluate diagonal neighbours as well
    :return: the final path the agent took from the beginning to the end.
    """
    #
    # the grid variable is the initial state; do stuff and set the solution to grid
    # grid goes grid[row][column]
    #
    start_coords, goal_coords = find_start_and_end(grid)
    # building priority queue for A* implementation
    frontier = []
    heapq.heappush(frontier, (0, start_coords))
    cost_so_far = {}
    cost_so_far[start_coords] = 0
    # path is similar in function to came_from dict in A* pseudocode
    path = [start_coords]

    while len(frontier) > 0:
        currentprio = heapq.heappop(frontier)
        priority = currentprio[0]
        current = currentprio[1]
        appended = False

        # checking if we started on the goal, if so immediately stop
        if current == goal_coords:
            break

        # checking if the current node is a valid neighbour of the last node
        if (accept_diags):
            if current != start_coords:
                # checking if this is a valid move
                if current in getneighboursdiag(grid, path[-1]) and current not in path:
                    path.append(current)
                    appended = True
                else:
                    heapq.heappush(frontier, (priority + 1, current))

            neighbours = getneighboursdiag(grid, current)
        else:
            if current != start_coords:
                # checking if this is a valid move
                if current in getneighbours(grid, path[-1]) and current not in path:
                    path.append(current)
                    appended = True
                else:
                    heapq.heappush(frontier, (priority + 1, current))

            neighbours = getneighbours(grid, current)

        if appended or current == start_coords:
            for neighbour in neighbours:
                # if we're one step from the goal, stop so as not to overwrite it
                if neighbour == goal_coords:
                    cost_so_far[neighbour] = 0
                    priority = 0
                    heapq.heappush(frontier, (priority, neighbour))
                    break

                # otherwise, update the queue to reflect newly discovered nodes 
                new_cost = cost_so_far[current] + 1
                if neighbour not in cost_so_far or new_cost > cost_so_far[neighbour]:
                    cost_so_far[neighbour] = new_cost
                    priority = new_cost + heuristic(goal_coords, neighbour)
                    clean_queue(frontier, neighbour)
                    heapq.heappush(frontier, (priority, neighbour))

    # popping start of path to not overwrite start coordinate
    path.pop(0)
    return path


def main():
    with open("pathfinding_a.txt", 'r') as f_input:
        grid = [[x for x in line if x != "\n"] for line in f_input.readlines()]


    path = astar(grid, False)

    grid_print(final_grid(path, grid))
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

    # file input
    with open("pathfinding_b.txt", 'r') as f_input:
        grid = [[x for x in line if x != "\n"] for line in f_input.readlines()]

    path = astar(grid, True)

    grid_print(final_grid(path, grid))
    # file output
    with open("pathfinding_b_out.txt", 'w') as f_output:
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
