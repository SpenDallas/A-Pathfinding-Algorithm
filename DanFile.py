'''
dan file bro
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
        return (x_start, y_start), (x_goal, y_goal)
    else:
        print("start or goal not found")




def main():
    # file input
    with open("pathfinding_a.txt", 'r') as f_input:
        grid = [[x for x in line if x != "\n"] for line in f_input.readlines()]

    #
    # the grid variable is the initial state; do stuff and set the solution to grid
    # grid goes grid[row][column]
    #
    start_coords, goal_coords = find_start_and_end(grid)
    print(start_coords, goal_coords)

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