"""
Test cases for 8-Puzzle algorithms
"""

TEST_CASES = {
    "easy": {
        "start": [[1, 2, 3], [4, 0, 5], [7, 8, 6]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 2
    },
    "medium": {
        "start": [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 2
    },
    "hard": {
        "start": [[0, 1, 3], [4, 2, 5], [7, 8, 6]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 4
    },
    "very_hard": {
        "start": [[8, 7, 6], [5, 4, 3], [2, 1, 0]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 31
    }
}

def run_all_tests(algorithm_func, algorithm_name):
    """Run algorithm on all test cases"""
    results = {}
    
    for difficulty, test_case in TEST_CASES.items():
        print(f"\nTesting {algorithm_name} on {difficulty} case...")
        result = algorithm_func(test_case["start"], test_case["goal"])
        results[difficulty] = result
        
        if result.get("solution_found", False):
            print(f"  ✓ Found solution in {result.get('path_length', 'N/A')} moves")
            print(f"  Nodes expanded: {result.get('nodes_expanded', 'N/A'):,}")
        else:
            print(f"  ✗ No solution found")
    
    return results

def is_solvable(puzzle):
    """Check if a puzzle configuration is solvable"""
    flat = [tile for row in puzzle for tile in row if tile != 0]
    inversions = 0
    
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    
    return inversions % 2 == 0

def print_puzzle(puzzle):
    """Print puzzle in readable format"""
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else " " for x in row))
