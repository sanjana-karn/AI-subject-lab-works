def calculate_heuristic(grid, player, opponent):
    """
    Calculate the heuristic value for a Tic-Tac-Toe grid.
    
    Args:
    grid (list of list): 3x3 Tic-Tac-Toe grid.
    player (str): Symbol for the player (e.g., 'X').
    opponent (str): Symbol for the opponent (e.g., 'O').
    
    Returns:
    int: Heuristic value e(p).
    """
    # Initialize open lines counts
    player_open_lines = 0
    opponent_open_lines = 0

    # Helper function to check if a line is open for a specific player
    def is_open(line, symbol):
        return all(cell == symbol or cell == ' ' for cell in line)

    # Check rows and columns
    for i in range(3):
        # Check rows
        row = grid[i]
        if is_open(row, player):
            player_open_lines += 1
        if is_open(row, opponent):
            opponent_open_lines += 1

        # Check columns
        col = [grid[j][i] for j in range(3)]
        if is_open(col, player):
            player_open_lines += 1
        if is_open(col, opponent):
            opponent_open_lines += 1

    # Check diagonals
    diag1 = [grid[i][i] for i in range(3)]
    diag2 = [grid[i][2 - i] for i in range(3)]

    if is_open(diag1, player):
        player_open_lines += 1
    if is_open(diag1, opponent):
        opponent_open_lines += 1

    if is_open(diag2, player):
        player_open_lines += 1
    if is_open(diag2, opponent):
        opponent_open_lines += 1

    # Calculate heuristic value
    heuristic_value = player_open_lines - opponent_open_lines
    return heuristic_value


# Example usage
if __name__ == "__main__":
    # Tic-Tac-Toe grid example (from the image)
    grid = [
        ['X', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player = 'X'
    opponent = 'O'

    heuristic = calculate_heuristic(grid, player, opponent)
    print("Heuristic value:", heuristic)
