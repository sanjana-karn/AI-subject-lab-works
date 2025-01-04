import heapq

class Puzzle:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state  # Initial state as a 2D list
        self.goal_state = goal_state    # Goal state as a 2D list

    def manhattan_distance(self, state):
        # Calculate the Manhattan Distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:  # Ignore the blank tile
                    x, y = divmod(state[i][j] - 1, 3)  # Goal position of the current tile
                    distance += abs(x - i) + abs(y - j)
        return distance

    def find_blank(self, state):
        # Locate the blank tile (0) in the grid
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_successors(self, state):
        # Generate all possible moves from the current state
        moves = []
        x, y = self.find_blank(state)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:  # Ensure the move is within bounds
                new_state = [row[:] for row in state]  # Copy the state
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]  # Swap tiles
                moves.append(new_state)

        return moves

    def solve(self):
        # Use A* search to solve the puzzle
        start = self.start_state
        goal = self.goal_state
        open_set = []  # Priority queue for A* search
        heapq.heappush(open_set, (0 + self.manhattan_distance(start), 0, start, []))
        visited = set()

        while open_set:
            _, g, current, path = heapq.heappop(open_set)
            if current == goal:
                return path + [current]  # Return the solution path
            visited.add(tuple(tuple(row) for row in current))

            for successor in self.generate_successors(current):
                if tuple(tuple(row) for row in successor) not in visited:
                    f = g + 1 + self.manhattan_distance(successor)
                    heapq.heappush(open_set, (f, g + 1, successor, path + [current]))

        return None  # No solution found


# Example Usage
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

puzzle = Puzzle(start_state, goal_state)
solution = puzzle.solve()

# Print the solution path
if solution:
    print("Solution Path:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
