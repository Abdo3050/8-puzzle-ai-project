
# Breadth-First Search (BFS) for 8-Puzzle

## Algorithm Overview
Breadth-First Search is an uninformed search algorithm that explores all nodes at the present depth level before moving on to nodes at the next depth level.

## Implementation Details

### Data Structures
- **Frontier**: Queue (FIFO)
- **Explored Set**: Hash set for visited states

### Key Features
- **Completeness**: Yes
- **Optimality**: Yes (for uniform cost)
- **Time Complexity**: O(b^d)
- **Space Complexity**: O(b^d)

## How to Use
```python
from bfs.bfs import bfs

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

result = bfs(start, goal)
if result["solution_found"]:
    print(f"Solution found in {result['path_length']} moves")
    print(f"Nodes expanded: {result['nodes_expanded']}")
