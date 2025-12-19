
#!/usr/bin/env python3
"""
Run complete analysis and generate final report
"""

import time
from bfs.bfs import bfs
from dfs.dfs import dfs
from ucs.ucs import ucs
from ids.ids import ids
from astar.astar import astar_search
from hill_climbing.hill_climbing import hill_climbing, hill_climbing_with_restart
from genetic_algorithm.genetic import genetic_algorithm_search
from report.analysis import PerformanceAnalyzer

# Standard test case
START_BOARD = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
GOAL_BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def main():
    """Run all algorithms and generate comprehensive report"""
    analyzer = PerformanceAnalyzer()
    
    print("Running 8-Puzzle Algorithm Analysis...")
    print("=" * 60)
    
    # Test BFS
    print("\n1. Running BFS...")
    start_time = time.time()
    bfs_result = bfs(START_BOARD, GOAL_BOARD)
    bfs_result["time_taken"] = time.time() - start_time
    analyzer.add_result("BFS", bfs_result)
    
    # Test DFS
    print("2. Running DFS...")
    start_time = time.time()
    dfs_result = dfs(START_BOARD, GOAL_BOARD)
    dfs_result["time_taken"] = time.time() - start_time
    analyzer.add_result("DFS", dfs_result)
    
    # Test UCS
    print("3. Running UCS...")
    start_time = time.time()
    ucs_result = ucs(START_BOARD, GOAL_BOARD)
    ucs_result["time_taken"] = time.time() - start_time
    analyzer.add_result("UCS", ucs_result)
    
    # Test IDS
    print("4. Running IDS...")
    start_time = time.time()
    ids_result = ids(START_BOARD, GOAL_BOARD)
    ids_result["time_taken"] = time.time() - start_time
    analyzer.add_result("IDS", ids_result)
    
    # Test A* Manhattan
    print("5. Running A* (Manhattan)...")
    start_time = time.time()
    astar_man_result = astar_search(START_BOARD, GOAL_BOARD, 'manhattan')
    astar_man_result["time_taken"] = time.time() - start_time
    analyzer.add_result("A* (Manhattan)", astar_man_result)
    
    # Test A* Misplaced
    print("6. Running A* (Misplaced)...")
    start_time = time.time()
    astar_mis_result = astar_search(START_BOARD, GOAL_BOARD, 'misplaced')
    astar_mis_result["time_taken"] = time.time() - start_time
    analyzer.add_result("A* (Misplaced)", astar_mis_result)
    
    # Test Hill Climbing
    print("7. Running Hill Climbing...")
    start_time = time.time()
    hc_result = hill_climbing(START_BOARD, GOAL_BOARD)
    hc_result["time_taken"] = time.time() - start_time
    analyzer.add_result("Hill Climbing", hc_result)
    
    # Test Hill Climbing with Restart
    print("8. Running Hill Climbing (Restart)...")
    start_time = time.time()
    hc_restart_result = hill_climbing_with_restart(START_BOARD, GOAL_BOARD)
    hc_restart_result["time_taken"] = time.time() - start_time
    analyzer.add_result("Hill Climbing (Restart)", hc_restart_result)
    
    # Test Genetic Algorithm
    print("9. Running Genetic Algorithm...")
    start_time = time.time()
    ga_result = genetic_algorithm_search(START_BOARD, GOAL_BOARD)
    ga_result["time_taken"] = time.time() - start_time
    analyzer.add_result("Genetic Algorithm", ga_result)
    
    # Generate reports
    print("\n" + "=" * 60)
    print("Generating Reports...")
    
    # Display comparison table
    print("\nCOMPARISON TABLE:")
    print(analyzer.generate_comparison_table().to_string())
    
    # Generate charts
    print("\nGenerating charts...")
    analyzer.plot_comparison_chart()
    analyzer.plot_fitness_progress(ga_result)
    
    # Save full report
    report_file = analyzer.save_report()
    print(f"\nFull report saved to: {report_file}")
    
    print("\n" + "=" * 60)
    print("Analysis Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
