from utils.state import PuzzleState
from utils.moves import get_possible_moves, get_path

def bfs(start_board, goal_board):
    """
    Breadth-First Search for 8-Puzzle
    :param start_board: Starting board configuration
    :param goal_board: Goal board configuration
    :return: Dictionary with results
    """
    start_state = PuzzleState(start_board)
    
    if start_state.board == goal_board:
        return {"path": [], "nodes_expanded": 0, "time": 0}
    
    # Initialize frontier and explored set
    frontier = [start_state]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        current_state = frontier.pop(0)  # FIFO queue
        
        # Check if goal is reached
        if current_state.board == goal_board:
            return {
                "path": get_path(current_state),
                "nodes_expanded": nodes_expanded,
                "path_length": current_state.g,
                "solution_found": True
            }
        
        # Add to explored set
        explored.add(tuple(map(tuple, current_state.board)))
        nodes_expanded += 1
        
        # Generate successors
        for move_name, next_state in get_possible_moves(current_state):
            board_tuple = tuple(map(tuple, next_state.board))
            if board_tuple not in explored:
                frontier.append(next_state)
    
    return {"solution_found": False, "nodes_expanded": nodes_expanded}
