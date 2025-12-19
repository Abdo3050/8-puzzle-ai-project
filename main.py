#!/usr/bin/env python3
"""
Main script to run 8-Puzzle algorithms with test cases
"""

import time
from test_cases import TEST_CASES, print_board, get_test_case
from bfs.bfs import bfs
from dfs.dfs import dfs
from ucs.ucs import ucs
from ids.ids import ids
from astar.astar import astar_search
from hill_climbing.hill_climbing import hill_climbing, hill_climbing_with_restart
from genetic_algorithm.genetic import genetic_algorithm_search

def run_algorithm(algorithm_name, algorithm_func, *args):
    """Run single algorithm and measure performance"""
    print(f"\n{'='*50}")
    print(f"Running {algorithm_name}")
    print(f"{'='*50}")
    
    start_time = time.time()
    result = algorithm_func(*args)
    end_time = time.time()
    
    result["time_taken"] = end_time - start_time
    
    if result.get("solution_found", False):
        print(f"✓ Solution found!")
        print(f"Path length: {result['path_length']}")
        print(f"Nodes expanded: {result.get('nodes_expanded', 'N/A')}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")

        # Show first and last few moves
        path = result.get('path')
        if path:
            print(f"First 5 moves: {[p[0] for p in path[:5]]}")
            if len(path) > 10:
                print(f"Last 5 moves: {[p[0] for p in path[-5:]]}")
    else:
        print(f"✗ No solution found")
        print(f"Nodes expanded: {result.get('nodes_expanded', 'N/A')}")
        print(f"Time taken: {result.get('time_taken', 0):.4f} seconds")
    
    return result

def main():
    """Main function"""
    print("8-Puzzle Solver - Test Suite")
    print("=" * 50)
    
    # Select test case
    print("\n📋 Available Test Cases:")
    for i, (name, case) in enumerate(TEST_CASES.items(), 1):
        print(f"{i}. {name:12} - {case['description']}")
    
    try:
        choice = int(input("\nEnter test case number (1-4): ").strip())
        case_names = list(TEST_CASES.keys())
        selected_case = case_names[choice-1] if 1 <= choice <= 4 else "easy"
    except (ValueError, IndexError):
        selected_case = "easy"
    
    test_case = TEST_CASES[selected_case]
    
    print(f"\nSelected Case: {selected_case}")
    print(f"Description: {test_case['description']}")
    print(f"Optimal length: {test_case['optimal_length']} moves")
    
    print("\nStart Board:")
    print_board(test_case["start"])
    
    print("\nGoal Board:")
    print_board(test_case["goal"])
    
    # Run all algorithms
    results = {}
    
    # 1. BFS
    results['BFS'] = run_algorithm("BFS", bfs, test_case["start"], test_case["goal"])
    
    # 2. DFS
    results['DFS'] = run_algorithm("DFS", dfs, test_case["start"], test_case["goal"])
    
    # 3. UCS
    results['UCS'] = run_algorithm("UCS", ucs, test_case["start"], test_case["goal"])
    
    # 4. IDS
    results['IDS'] = run_algorithm("IDS", ids, test_case["start"], test_case["goal"])
    
    # 5. A* Manhattan
    results['A* Manhattan'] = run_algorithm("A* (Manhattan)", astar_search, 
                                          test_case["start"], test_case["goal"], 'manhattan')
    
    # 6. A* Misplaced
    results['A* Misplaced'] = run_algorithm("A* (Misplaced)", astar_search,
                                          test_case["start"], test_case["goal"], 'misplaced')
    
    # 7. Hill Climbing
    results['Hill Climbing'] = run_algorithm("Hill Climbing", hill_climbing,
                                           test_case["start"], test_case["goal"])
    
    # 8. Hill Climbing with Restart
    results['Hill Climbing (Restart)'] = run_algorithm("Hill Climbing (Restart)", 
                                                      hill_climbing_with_restart,
                                                      test_case["start"], test_case["goal"])
    #Abdelrhman Reda Abdelrhman Torad
    # 9. Genetic Algorithm
    results['Genetic Algorithm'] = run_algorithm("Genetic Algorithm", genetic_algorithm_search,
                                               test_case["start"], test_case["goal"])
    
    # Display comparison table
    print("\n" + "="*70)
    print("COMPARISON TABLE")
    print("="*70)
    print(f"{'Algorithm':<25} {'Time (s)':<10} {'Nodes':<10} {'Path Len':<10} {'Found':<10}")
    print("-"*70)
    
    for algo_name, result in results.items():
        time_taken = result.get('time_taken', 0)
        nodes = result.get('nodes_expanded', 'N/A')
        path_len = result.get('path_length', 'N/A')
        found = '✓' if result.get('solution_found', False) else '✗'
        
        print(f"{algo_name:<25} {time_taken:<10.4f} {nodes:<10} {path_len:<10} {found:<10}")

if __name__ == "__main__":
    main()
