#!/usr/bin/env python3
"""
Main script to run 8-Puzzle algorithms
"""

import time
from bfs.bfs import bfs
from dfs.dfs import dfs
from ucs.ucs import ucs
from ids.ids import ids
from astar.astar import astar_search
from hill_climbing.hill_climbing import hill_climbing, hill_climbing_with_restart

# Test puzzle configurations
START_BOARD = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

GOAL_BOARD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def print_board(board):
    """Print puzzle board nicely"""
    print("+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("   |", end="")
            else:
                print(f" {cell} |", end="")
        print("\n+---+---+---+")

def run_algorithm(algorithm_name, algorithm_func, *args):
    """Run algorithm and measure time"""
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
        print(f"Nodes expanded: {result['nodes_expanded']}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")
        
        # Show first and last few moves
        path = result['path']
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
    print("8-Puzzle Solver")
    print("=" * 50)
    print("Start board:")
    print_board(START_BOARD)
    print("\nGoal board:")
    print_board(GOAL_BOARD)
    
    results = {}
    
    # Run BFS
    results['BFS'] = run_algorithm("BFS", bfs, START_BOARD, GOAL_BOARD)
    
    # Run DFS
    results['DFS'] = run_algorithm("DFS", dfs, START_BOARD, GOAL_BOARD)
    
    # Run UCS
    results['UCS'] = run_algorithm("UCS", ucs, START_BOARD, GOAL_BOARD)
    
    # Run IDS
    results['IDS'] = run_algorithm("IDS", ids, START_BOARD, GOAL_BOARD)
    
    # Run A* with Manhattan
    results['A* Manhattan'] = run_algorithm("A* (Manhattan)", astar_search, START_BOARD, GOAL_BOARD, 'manhattan')
    
    # Run A* with Misplaced
    results['A* Misplaced'] = run_algorithm("A* (Misplaced)", astar_search, START_BOARD, GOAL_BOARD, 'misplaced')
    
    # Run Hill Climbing
    results['Hill Climbing'] = run_algorithm("Hill Climbing", hill_climbing, START_BOARD, GOAL_BOARD)
    
    # Run Hill Climbing with Restart
    results['Hill Climbing (Restart)'] = run_algorithm("Hill Climbing (Restart)", hill_climbing_with_restart, START_BOARD, GOAL_BOARD)
    
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
