# A* Search for 8-Puzzle

## Algorithm Overview
A* Search is an informed search algorithm that uses a heuristic function to estimate the cost to reach the goal from a given state.

## Implementation Details

### Heuristics
1. **Manhattan Distance**: Sum of vertical and horizontal distances
2. **Misplaced Tiles**: Count of tiles in wrong positions

### Data Structures
- **Open List**: Priority queue (min-heap) sorted by f = g + h
- **Closed Set**: Visited states
- **Open Dict**: For quick lookups

### Key Features
- **Completeness**: Yes (with admissible heuristic)
- **Optimality**: Yes (with admissible heuristic)
- **Time Complexity**: Depends on heuristic quality
- **Space Complexity**: O(b^d)

## How to Use
```python
from astar.astar import astar_search

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

# With Manhattan Distance
result = astar_search(start, goal, heuristic='manhattan')

# With Misplaced Tiles
result = astar_search(start, goal, heuristic='misplaced')
