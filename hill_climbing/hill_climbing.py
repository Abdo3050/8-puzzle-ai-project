import random
from utils.state import PuzzleState
from utils.moves import get_possible_moves
from utils.heuristics import manhattan_distance

def hill_climbing(start_board, goal_board, max_iterations=1000):
    """
    Hill Climbing for 8-Puzzle
    :param start_board: Starting board configuration
    :param goal_board: Goal board configuration
    :param max_iterations: Maximum number of iterations
    :return: Dictionary with results
    """
    current_state = PuzzleState(start_board)
    current_h = manhattan_distance(current_state, goal_board)
    
    path = []
    nodes_expanded = 0
    
    for iteration in range(max_iterations):
        # Check if goal is reached
        if current_state.board == goal_board:
            return {
                "path": path,
                "nodes_expanded": nodes_expanded,
                "path_length": len(path),
                "solution_found": True,
                "iterations": iteration + 1
            }
        
        # Get all possible moves
        moves = get_possible_moves(current_state)
        nodes_expanded += len(moves)
        
        # Find the best neighbor
        best_neighbor = None
        best_h = current_h
        
        for move_name, next_state in moves:
            h = manhattan_distance(next_state, goal_board)
            if h < best_h:
                best_h = h
                best_neighbor = (move_name, next_state)
        
        # If no better neighbor, we're at a local optimum
        if best_neighbor is None:
            return {
                "solution_found": False,
                "nodes_expanded": nodes_expanded,
                "final_h": current_h,
                "iterations": iteration + 1,
                "local_optimum": True
            }
        
        # Move to the best neighbor
        move_name, next_state = best_neighbor
        path.append(move_name)
        current_state = next_state
        current_h = best_h
    
    return {
        "solution_found": False,
        "nodes_expanded": nodes_expanded,
        "iterations": max_iterations,
        "max_iterations_reached": True
    }

def hill_climbing_with_restart(start_board, goal_board, restarts=10, max_iterations=500):
    """
    Hill Climbing with Random Restart
    """
    best_solution = None
    best_h = float('inf')
    
    for restart in range(restarts):
        result = hill_climbing(start_board, goal_board, max_iterations)
        
        if result["solution_found"]:
            return result
        
        # Keep track of best solution found
        if "final_h" in result and result["final_h"] < best_h:
            best_h = result["final_h"]
            best_solution = result
    
    return best_solution or {"solution_found": False}
