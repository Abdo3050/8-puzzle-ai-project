# Hill Climbing for 8-Puzzle

## Algorithm Overview
Hill Climbing is a local search algorithm that continuously moves in the direction of increasing elevation (or decreasing heuristic value) to find the peak (optimal solution).

## Variants
1. **Steepest Ascent**: Always chooses the best neighbor
2. **Random Restart**: Restarts from random positions to escape local optima

## Implementation Details

### Heuristic
- **Manhattan Distance**: Used to evaluate states

### Data Structures
- **Current State**: Single state being evaluated
- **Neighbors**: All possible moves from current state

### Key Features
- **Completeness**: No (may get stuck in local optima)
- **Optimality**: No
- **Time Complexity**: O(b * iterations)
- **Space Complexity**: O(1)

## How to Use
```python
from hill_climbing.hill_climbing import hill_climbing, hill_climbing_with_restart

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

# Basic Hill Climbing
result = hill_climbing(start, goal, max_iterations=1000)

# With Random Restart
result = hill_climbing_with_restart(start, goal, restarts=10)
