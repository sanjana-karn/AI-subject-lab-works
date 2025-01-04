import heapq

class NPuzzleSolver:
    def __init__(self, start, goal):
        self.start = start  # Initial state
        self.goal = goal  # Goal state
        self.n = len(start)  # Puzzle size (n x n)

    def manhattan_distance(self, state):
        """
        Calculate the Manhattan distance heuristic.
        """
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0:  # Ignore the blank space
                    x, y = divmod(state[i][j] - 1, self.n)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def get_neighbors(self, state):
        """
        Generate all valid neighbors of the current state.
        """
        neighbors = []
        x, y = next((i, j) for i in range(self.n) for j in range(self.n) if state[i][j] == 0)  # Find blank tile

        # Possible moves: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:  # Check if move is within bounds
                # Swap blank tile with neighbor
                new_state = [row[:] for row in state]  # Copy state
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                neighbors.append(new_state)

        return neighbors

    def solve(self):
        """
        Solve the n-Puzzle using A* search algorithm.
        """
        # Priority queue for A* search
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.start, 0, None))  # (f(n), state, g(n), parent)

        visited = set()
        parent_map = {}  # To reconstruct the path

        while priority_queue:
            f, current, g, parent = heapq.heappop(priority_queue)

            # Mark as visited
            current_tuple = tuple(tuple(row) for row in current)
            if current_tuple in visited:
                continue
            visited.add(current_tuple)
            parent_map[current_tuple] = parent

            # Check if the goal is reached
            if current == self.goal:
                return g  # Return number of moves to reach the goal

            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited:
                    h = self.manhattan_distance(neighbor)
                    heapq.heappush(priority_queue, (g + 1 + h, neighbor, g + 1, current_tuple))

        return -1  # Return -1 if no solution is found


# Example usage
if __name__ == "__main__":
    # Define start and goal states
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

    solver = NPuzzleSolver(start_state, goal_state)
    moves = solver.solve()
    print("Number of moves to solve the puzzle:", moves)
