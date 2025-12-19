from utils.state import PuzzleState
from utils.moves import get_possible_moves, get_path

def dfs(start_board, goal_board, max_depth=50):
    """
    Depth-First Search for 8-Puzzle with depth limit
    :param start_board: Starting board configuration
    :param goal_board: Goal board configuration
    :param max_depth: Maximum depth to search
    :return: Dictionary with results
    """
    start_state = PuzzleState(start_board)
    
    if start_state.board == goal_board:
        return {"path": [], "nodes_expanded": 0}
    
    # Initialize stack with (state, depth)
    stack = [(start_state, 0)]
    explored = set()
    nodes_expanded = 0
    
    while stack:
        current_state, depth = stack.pop()  # LIFO stack
        
        # Check if goal is reached
        if current_state.board == goal_board:
            return {
                "path": get_path(current_state),
                "nodes_expanded": nodes_expanded,
                "path_length": current_state.g,
                "solution_found": True
            }
        
        # Check depth limit
        if depth >= max_depth:
            continue
        
        # Add to explored set
        explored.add(tuple(map(tuple, current_state.board)))
        nodes_expanded += 1
        
        # Generate successors
        for move_name, next_state in get_possible_moves(current_state):
            board_tuple = tuple(map(tuple, next_state.board))
            if board_tuple not in explored:
                stack.append((next_state, depth + 1))
    
    return {"solution_found": False, "nodes_expanded": nodes_expanded}
