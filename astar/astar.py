import heapq
from utils.state import PuzzleState
from utils.moves import get_possible_moves, get_path
from utils.heuristics import manhattan_distance, misplaced_tiles

def astar_search(start_board, goal_board, heuristic='manhattan'):
    """
    A* Search for 8-Puzzle
    :param start_board: Starting board configuration
    :param goal_board: Goal board configuration
    :param heuristic: 'manhattan' or 'misplaced'
    :return: Dictionary with results
    """
    start_state = PuzzleState(start_board)
    
    if start_state.board == goal_board:
        return {"path": [], "nodes_expanded": 0}
    
    # Choose heuristic function
    if heuristic == 'manhattan':
        h_func = lambda s: manhattan_distance(s, goal_board)
    else:
        h_func = lambda s: misplaced_tiles(s, goal_board)
    
    # Initialize start state
    start_state.h = h_func(start_state)
    start_state.f = start_state.g + start_state.h
    
    # Priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (start_state.f, start_state))
    
    # Dictionaries for tracking
    open_dict = {tuple(map(tuple, start_state.board)): start_state}
    closed_set = set()
    
    nodes_expanded = 0
    
    while open_list:
        # Get state with lowest f value
        current_f, current_state = heapq.heappop(open_list)
        current_key = tuple(map(tuple, current_state.board))
        
        # Remove from open_dict
        if current_key in open_dict:
            del open_dict[current_key]
        
        # Check if goal is reached
        if current_state.board == goal_board:
            return {
                "path": get_path(current_state),
                "nodes_expanded": nodes_expanded,
                "path_length": current_state.g,
                "solution_found": True
            }
        
        # Add to closed set
        closed_set.add(current_key)
        nodes_expanded += 1
        
        # Generate successors
        for move_name, next_state in get_possible_moves(current_state):
            next_key = tuple(map(tuple, next_state.board))
            
            # Skip if in closed set
            if next_key in closed_set:
                continue
            
            # Calculate f value
            next_state.h = h_func(next_state)
            next_state.f = next_state.g + next_state.h
            
            # Check if in open list with better g value
            if next_key in open_dict:
                existing_state = open_dict[next_key]
                if next_state.g < existing_state.g:
                    # Update the state in open list
                    existing_state.g = next_state.g
                    existing_state.f = next_state.g + existing_state.h
                    existing_state.parent = current_state
                    existing_state.move = move_name
                    
                    # Re-heapify
                    heapq.heapify(open_list)
            else:
                # Add to open list
                heapq.heappush(open_list, (next_state.f, next_state))
                open_dict[next_key] = next_state
    
    return {"solution_found": False, "nodes_expanded": nodes_expanded}
