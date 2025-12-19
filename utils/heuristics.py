def manhattan_distance(state, goal_board):
    """
    Calculate Manhattan distance heuristic
    :param state: Current PuzzleState
    :param goal_board: Goal board configuration
    :return: Manhattan distance
    """
    distance = 0
    
    # Create a dictionary for goal positions
    goal_positions = {}
    for i in range(3):
        for j in range(3):
            goal_positions[goal_board[i][j]] = (i, j)
    
    # Calculate Manhattan distance for each tile
    for i in range(3):
        for j in range(3):
            tile = state.board[i][j]
            if tile != 0:  # Skip blank tile
                goal_i, goal_j = goal_positions[tile]
                distance += abs(i - goal_i) + abs(j - goal_j)
    
    return distance

def misplaced_tiles(state, goal_board):
    """
    Calculate number of misplaced tiles heuristic
    :param state: Current PuzzleState
    :param goal_board: Goal board configuration
    :return: Number of misplaced tiles
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0 and state.board[i][j] != goal_board[i][j]:
                count += 1
    return count

def linear_conflict(state, goal_board):
    """
    Calculate linear conflict heuristic (Manhattan + conflicts)
    """
    # Start with Manhattan distance
    distance = manhattan_distance(state, goal_board)
    
    # Add linear conflicts in rows
    for i in range(3):
        row_tiles = []
        for j in range(3):
            tile = state.board[i][j]
            if tile != 0:
                goal_i, goal_j = None, None
                for x in range(3):
                    for y in range(3):
                        if goal_board[x][y] == tile:
                            goal_i, goal_j = x, y
                            break
                if goal_i == i:  # Tile belongs in this row
                    row_tiles.append((tile, goal_j))
        
        # Check for conflicts
        for k in range(len(row_tiles)):
            for l in range(k + 1, len(row_tiles)):
                if row_tiles[k][1] > row_tiles[l][1]:
                    distance += 2  # Each conflict adds 2
    
    # Add linear conflicts in columns
    for j in range(3):
        col_tiles = []
        for i in range(3):
            tile = state.board[i][j]
            if tile != 0:
                goal_i, goal_j = None, None
                for x in range(3):
                    for y in range(3):
                        if goal_board[x][y] == tile:
                            goal_i, goal_j = x, y
                            break
                if goal_j == j:  # Tile belongs in this column
                    col_tiles.append((tile, goal_i))
        
        # Check for conflicts
        for k in range(len(col_tiles)):
            for l in range(k + 1, len(col_tiles)):
                if col_tiles[k][1] > col_tiles[l][1]:
                    distance += 2
    
    return distance
