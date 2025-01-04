class BlocksWorld:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state  # Current arrangement of blocks
        self.goal_state = goal_state    # Goal arrangement of blocks

    def calculate_heuristic(self):
        heuristic_value = 0
        n = len(self.start_state)

        # Compare blocks in the start and goal state
        for i in range(n - 1):  # Exclude the topmost block from comparison
            if self.start_state[i + 1] == self.goal_state[i]:  # Correct support
                heuristic_value += 1
            else:  # Incorrect support
                heuristic_value -= 1

        return heuristic_value


# Start and Goal States
start_state = ["A", "D", "C", "B"]  # From top to bottom
goal_state = ["D", "C", "B", "A"]   # From top to bottom

# Create a BlocksWorld instance
blocks_world = BlocksWorld(start_state, goal_state)

# Calculate and print the heuristic value
heuristic_value = blocks_world.calculate_heuristic()
print("Heuristic Value:", heuristic_value)
