class WaterJug:
    def __init__(self, capacity, goal):
        # Initialize jug capacities and the goal state
        self.capacity = capacity  # (4, 3)
        self.goal = goal          # (2, 0)

    def goal_test(self, state):
        # Check if the current state matches the goal state
        return state == self.goal

    def successors(self, state):
        # Generate all possible states from the current state
        j1, j2 = self.capacity
        x, y = state
        return list(set([
            (j1, y),           # Fill jug 1
            (x, j2),           # Fill jug 2
            (0, y),            # Empty jug 1
            (x, 0),            # Empty jug 2
            (max(0, x - (j2 - y)), min(j2, x + y)),  # Pour from jug 1 to jug 2
            (min(j1, x + y), max(0, y - (j1 - x)))   # Pour from jug 2 to jug 1
        ]))

    def dfs(self):
        # Perform a depth-first search to find the solution
        stack, visited = [(0, 0)], set()
        parent = {}  # Keep track of the parent state for backtracking

        while stack:
            state = stack.pop()
            if self.goal_test(state):
                # Backtrack to find the solution path
                path = []
                while state:
                    path.append(state)
                    state = parent.get(state)
                return path[::-1]  # Reverse the path to get start-to-goal order

            if state not in visited:
                visited.add(state)
                for succ in self.successors(state):
                    if succ not in visited:
                        parent[succ] = state
                        stack.append(succ)

        return None  # No solution found

# Example usage
water_jug = WaterJug((4, 3), (2, 0))
solution = water_jug.dfs()
print("Solution Path:", solution)
