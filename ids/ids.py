from utils.state import PuzzleState
from utils.moves import get_possible_moves, get_path

def depth_limited_dfs(state, goal_board, depth_limit, explored, nodes_expanded):
    """
    Depth Limited DFS helper function
    """
    # Check if goal is reached
    if state.board == goal_board:
        return {
            "state": state,
            "nodes_expanded": nodes_expanded,
            "found": True
        }
    
    # Check depth limit
    if depth_limit <= 0:
        return {"found": False, "nodes_expanded": nodes_expanded}
    
    # Add to explored set
    explored.add(tuple(map(tuple, state.board)))
    nodes_expanded[0] += 1
    
    # Generate successors
    for move_name, next_state in get_possible_moves(state):
        next_key = tuple(map(tuple, next_state.board))
        
        if next_key not in explored:
            result = depth_limited_dfs(next_state, goal_board, depth_limit - 1, explored, nodes_expanded)
            if result["found"]:
                return result
    
    return {"found": False, "nodes_expanded": nodes_expanded[0]}

def ids(start_board, goal_board, max_depth=50):
    """
    Iterative Deepening Search for 8-Puzzle
    """
    start_state = PuzzleState(start_board)
    
    if start_state.board == goal_board:
        return {"path": [], "nodes_expanded": 0}
    
    total_nodes_expanded = 0
    
    for depth in range(max_depth + 1):
        explored = set()
        nodes_expanded = [0]
        
        result = depth_limited_dfs(
            start_state, 
            goal_board, 
            depth, 
            explored, 
            nodes_expanded
        )
        
        total_nodes_expanded += nodes_expanded[0]
        
        if result["found"]:
            return {
                "path": get_path(result["state"]),
                "nodes_expanded": total_nodes_expanded,
                "path_length": result["state"].g,
                "depth_limit": depth,
                "solution_found": True
            }
    
    return {"solution_found": False, "nodes_expanded": total_nodes_expanded}
