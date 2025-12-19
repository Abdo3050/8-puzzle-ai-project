# Uniform Cost Search (UCS) for 8-Puzzle

## Algorithm Overview
Uniform Cost Search is an uninformed search algorithm that expands the node with the lowest path cost first.

## Implementation Details

### Data Structures
- **Frontier**: Priority Queue (min-heap)
- **Explored Set**: Hash set for visited states
- **Cost Function**: g(n) = path cost from start

### Key Features
- **Completeness**: Yes
- **Optimality**: Yes
- **Time Complexity**: O(b^(1+⌊C*/ε⌋))
- **Space Complexity**: O(b^(1+⌊C*/ε⌋))

## How to Use
```python
from ucs.ucs import ucs

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

result = ucs(start, goal)
if result["solution_found"]:
    print(f"Optimal solution found with cost {result['path_length']}")
