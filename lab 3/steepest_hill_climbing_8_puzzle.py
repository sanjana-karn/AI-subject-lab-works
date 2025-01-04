class PuzzleHillClimbing:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def heuristic(self, state):
        # Heuristic: Count the number of misplaced tiles
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != self.goal_state[i][j]:
                    misplaced += 1
        return misplaced

    def find_blank(self, state):
        # Locate the blank tile (0) in the grid
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_successors(self, state):
        # Generate all possible states by moving the blank tile
        moves = []
        x, y = self.find_blank(state)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:  # Check bounds
                new_state = [row[:] for row in state]  # Copy the state
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]  # Swap tiles
                moves.append(new_state)

        return moves

    def steepest_ascent(self):
        current = self.start_state
        current_heuristic = self.heuristic(current)

        while True:
            successors = self.generate_successors(current)
            best_successor = None
            best_heuristic = float("inf")

            for successor in successors:
                h = self.heuristic(successor)
                if h < best_heuristic:
                    best_successor = successor
                    best_heuristic = h

            # If no improvement, terminate
            if best_heuristic >= current_heuristic:
                return current, current_heuristic

            # Move to the best successor
            current = best_successor
            current_heuristic = best_heuristic

# Example usage
start_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

puzzle = PuzzleHillClimbing(start_state, goal_state)
final_state, final_heuristic = puzzle.steepest_ascent()

# Print results
print("Final State:")
for row in final_state:
    print(row)
print(f"Heuristic Value: {final_heuristic}")
