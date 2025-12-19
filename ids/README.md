# Iterative Deepening Search (IDS) for 8-Puzzle

## Algorithm Overview
Iterative Deepening Search combines the benefits of DFS and BFS by performing DFS with increasing depth limits.

## Implementation Details

### Data Structures
- **Recursive DFS**: With depth limit
- **Explored Set**: For each iteration
- **Iteration**: Increasing depth limit

### Key Features
- **Completeness**: Yes
- **Optimality**: Yes (for uniform cost)
- **Time Complexity**: O(b^d)
- **Space Complexity**: O(bd)

## How to Use
```python
from ids.ids import ids

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

result = ids(start, goal, max_depth=31)
if result["solution_found"]:
    print(f"Solution found at depth {result['depth_limit']}")
