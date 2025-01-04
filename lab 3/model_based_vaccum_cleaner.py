import random

class ModelBasedVacuumAgent:
    def __init__(self, grid_size=(10, 10)):
        # Initialize the grid environment and the internal model
        self.grid_size = grid_size
        self.grid = [[random.choice([0, 1]) for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.model = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]
        self.position = (0, 0)  # Starting position

    def print_grid(self, grid):
        for row in grid:
            print(row)
        print()

    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 1:
            self.grid[x][y] = 0  # Clean the cell
        self.model[x][y] = 1  # Mark cell as visited in the model

    def move(self):
        x, y = self.position
        if y < self.grid_size[1] - 1:
            self.position = (x, y + 1)  # Move right
        elif x < self.grid_size[0] - 1:
            self.position = (x + 1, 0)  # Move down to the next row

    def run(self):
        print("Initial Grid:")
        self.print_grid(self.grid)
        for _ in range(self.grid_size[0] * self.grid_size[1]):
            self.clean()
            self.move()
        print("Cleaned Grid:")
        self.print_grid(self.grid)

# Example usage:
agent = ModelBasedVacuumAgent(grid_size=(10, 10))
agent.run()
