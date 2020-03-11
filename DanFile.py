'''
dan file bro
'''


def main():
    # file input
    with open("pathfinding_a.txt", 'r') as f_input:
        grid = [[x for x in line if x != "\n"] for line in f_input.readlines()]

    #
    # the grid variable is the initial state; do stuff and set the solution to grid
    #

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