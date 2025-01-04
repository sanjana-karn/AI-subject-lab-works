import random

def reflex_vacuum_agent(grid_size=(10, 10)):
    # Initializing the grid with random clean (0) and dirty (1) states
    grid = [[random.choice([0, 1]) for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    position = (0, 0)  # Starting at the top-left corner

    # Function to print the grid
    def print_grid():
        for row in grid:
            print(row)
        print()

    print("Initial Grid:")
    print_grid()

    # Cleaning the grid
    for _ in range(grid_size[0] * grid_size[1]):
        x, y = position
        if grid[x][y] == 1:
            grid[x][y] = 0  # Cleaning the current location
        # Moving to the next position
        if y < grid_size[1] - 1:  # Moving right
            position = (x, y + 1)
        elif x < grid_size[0] - 1:  # Moving down to the next row
            position = (x + 1, 0)

    print("Cleaned Grid:")
    print_grid()

# Running the reflex vacuum agent for a 10x10 grid
reflex_vacuum_agent(grid_size=(10, 10))
