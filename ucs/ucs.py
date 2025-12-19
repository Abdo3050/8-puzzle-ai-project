import heapq
from utils.state import PuzzleState
from utils.moves import get_possible_moves, get_path

def ucs(start_board, goal_board):
    """
    Uniform Cost Search for 8-Puzzle
    """
    start_state = PuzzleState(start_board)
    
    if start_state.board == goal_board:
        return {"path": [], "nodes_expanded": 0}
    
    # Priority queue (min-heap) based on g cost
    frontier = []
    heapq.heappush(frontier, (start_state.g, start_state))
    
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        current_cost, current_state = heapq.heappop(frontier)
        
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
            next_key = tuple(map(tuple, next_state.board))
            
            if next_key not in explored:
                # Check if already in frontier with higher cost
                in_frontier = False
                for cost, state in frontier:
                    if tuple(map(tuple, state.board)) == next_key:
                        in_frontier = True
                        if next_state.g < state.g:
                            # Remove old entry and add new one
                            frontier.remove((cost, state))
                            heapq.heapify(frontier)
                            heapq.heappush(frontier, (next_state.g, next_state))
                        break
                
                if not in_frontier:
                    heapq.heappush(frontier, (next_state.g, next_state))
    
    return {"solution_found": False, "nodes_expanded": nodes_expanded}
