# Genetic Algorithm for 8-Puzzle

## Algorithm Overview
Genetic Algorithm is a population-based metaheuristic inspired by natural selection. It evolves a population of candidate solutions over generations.

## Genetic Operators

### 1. Representation
- **Chromosome**: Sequence of moves (Up, Down, Left, Right)
- **Length**: Variable (10-50 moves)

### 2. Fitness Function
- Based on Manhattan Distance to goal
- Inverse of distance (higher is better)
- Penalty for longer chromosomes

### 3. Selection
- **Tournament Selection**: Size 3
- Elitism: Keep top 10% of population

### 4. Crossover
- **Single-point Crossover**
- Crossover rate: 70%

### 5. Mutation
- **Point Mutation**: Change random moves
- **Insertion/Deletion**: Add or remove moves
- Mutation rate: 15%

## Key Features
- **Completeness**: Yes (given enough time)
- **Optimality**: No guarantee
- **Time Complexity**: O(population * generations * chromosome_length)
- **Space Complexity**: O(population * chromosome_length)

## How to Use
```python
from genetic_algorithm.genetic import genetic_algorithm_search

start = [[1,2,3],[4,0,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

result = genetic_algorithm_search(start, goal)
if result["solution_found"]:
    print(f"Solution found in {result['generations']} generations")
