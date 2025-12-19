from utils.state import PuzzleState

def get_possible_moves(state):
    """
    Generate all possible next states from current state
    :param state: Current PuzzleState
    :return: List of (move_direction, new_state) tuples
    """
    moves = []
    blank_row, blank_col = state.get_blank_position()
    
    # Directions: Up, Down, Left, Right
    directions = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]
    
    for move_name, row_change, col_change in directions:
        new_row = blank_row + row_change
        new_col = blank_col + col_change
        
        # Check if move is within bounds
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Create new board
            new_board = state.get_copy()
            
            # Swap blank with target tile
            new_board[blank_row][blank_col] = new_board[new_row][new_col]
            new_board[new_row][new_col] = 0
            
            # Create new state
            new_state = PuzzleState(
                board=new_board,
                parent=state,
                move=move_name,
                g=state.g + 1  # Each move costs 1
            )
            
            moves.append((move_name, new_state))
    
    return moves

def get_path(state):
    """
    Get the path from start to goal state
    :param state: Goal state
    :return: List of moves and states
    """
    path = []
    current = state
    
    while current is not None:
        path.append((current.move, current.board))
        current = current.parent
    
    path.reverse()  # From start to goal
    return path[1:]  # Remove the first (no move)

def apply_move(board, move):
    """Apply a move to a board and return new board"""
    new_board = [row[:] for row in board]
    blank_pos = None
    
    # Find blank position
    for i in range(3):
        for j in range(3):
            if new_board[i][j] == 0:
                blank_pos = (i, j)
                break
        if blank_pos:
            break
    
    if not blank_pos:
        return board
    
    i, j = blank_pos
    
    # Apply move
    if move == 'Up' and i > 0:
        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
    elif move == 'Down' and i < 2:
        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
    elif move == 'Left' and j > 0:
        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
    elif move == 'Right' and j < 2:
        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    
    return new_board
