"""
Test cases for 8-Puzzle algorithms
"""

TEST_CASES = {
    "easy": {
        "start": [[1, 2, 3], [4, 0, 5], [7, 8, 6]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 2,
        "description": "Easy case - requires 2 moves"
    },
    "medium": {
        "start": [[1, 2, 3], [4, 5, 6], [0, 7, 8]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 2,
        "description": "Medium difficulty case"
    },
    "hard": {
        "start": [[0, 1, 3], [4, 2, 5], [7, 8, 6]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 4,
        "description": "Hard case - requires 4 moves"
    },
    "very_hard": {
        "start": [[8, 7, 6], [5, 4, 3], [2, 1, 0]],
        "goal": [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
        "optimal_length": 31,
        "description": "Hardest case - 31 moves (maximum)"
    }
}

def print_board(board):
    """Print puzzle board in readable format"""
    print("+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("   |", end="")
            else:
                print(f" {cell} |", end="")
        print("\n+---+---+---+")

def run_all_tests(algorithm_func, algorithm_name, selected_cases=None):
    """Run algorithm on selected test cases"""
    if selected_cases is None:
        selected_cases = list(TEST_CASES.keys())

    results = {}

    for difficulty in selected_cases:
        if difficulty in TEST_CASES:
            test_case = TEST_CASES[difficulty]
            print(f"\nTesting {algorithm_name} on {difficulty} case...")
            print(f"Description: {test_case['description']}")

            result = algorithm_func(test_case["start"], test_case["goal"])
            results[difficulty] = result

            if result.get("solution_found", False):
                print(f"  ✓ Solution found!")
                print(f"  Path length: {result.get('path_length', 'N/A')}")
                nodes = result.get('nodes_expanded', 'N/A')
                if isinstance(nodes, int):
                    print(f"  Nodes expanded: {nodes:,}")
                else:
                    print(f"  Nodes expanded: {nodes}")
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

def get_test_case(name):
    """Get a specific test case by name"""
    return TEST_CASES.get(name, TEST_CASES["easy"])