# Depth-First Search (DFS) for 8-Puzzle

## Algorithm Overview
Depth-First Search is an uninformed search algorithm that explores as far as possible along each branch before backtracking.

## Implementation Details

### Data Structures
- **Frontier**: Stack (LIFO)
- **Explored Set**: Hash set for visited states
- **Depth Limit**: Prevents infinite loops

### Key Features
- **Completeness**: No (without depth limit)
- **Optimality**: No
- **Time Complexity**: O(b^m)
- **Space Complexity**: O(bm)

## How to Use
```python
from dfs.dfs import dfs

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

# With depth limit (default 50)
result = dfs(start, goal, max_depth=50)

# Without depth limit (not recommended)
result = dfs(start, goal, max_depth=1000)
