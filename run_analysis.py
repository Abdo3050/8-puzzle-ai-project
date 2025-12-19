#!/usr/bin/env python3
"""
Comprehensive analysis of all algorithms on all test cases
"""

import time
from datetime import datetime
from test_cases import TEST_CASES, run_all_tests
from bfs.bfs import bfs
from dfs.dfs import dfs
from ucs.ucs import ucs
from ids.ids import ids
from astar.astar import astar_search
from hill_climbing.hill_climbing import hill_climbing, hill_climbing_with_restart
from genetic_algorithm.genetic import genetic_algorithm_search
from report.analysis import PerformanceAnalyzer

def comprehensive_analysis():
    """Run comprehensive analysis across all algorithms and test cases"""

    print("8-Puzzle Algorithm Comprehensive Analysis")
    print("=" * 60)
    print(f"Analysis started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Test case selection
    print("\nAvailable test cases:")
    case_names = list(TEST_CASES.keys())
    for i, case_name in enumerate(case_names, 1):
        case_info = TEST_CASES[case_name]
        print(f"{i}. {case_name} - {case_info['description']}")

    while True:
        try:
            user_input = input("\nEnter case numbers (1-4) separated by commas, or press Enter for all cases: ").strip()
            if not user_input:
                selected_indices = list(range(len(case_names)))
                break
            else:
                selected_indices = []
                for num in user_input.split(','):
                    num = num.strip()
                    if num.isdigit():
                        idx = int(num) - 1
                        if 0 <= idx < len(case_names):
                            selected_indices.append(idx)
                        else:
                            print(f"Invalid case number: {int(num)}. Please enter numbers between 1 and {len(case_names)}.")
                            selected_indices = []
                            break
                    else:
                        print(f"Invalid input: '{num}'. Please enter numbers only.")
                        selected_indices = []
                        break
                if selected_indices:
                    break
        except KeyboardInterrupt:
            print("\nAnalysis cancelled.")
            return {}, []

    selected_cases = [case_names[i] for i in selected_indices]
    print(f"\nSelected test cases: {', '.join(selected_cases)}")

    # Define all algorithms to test
    algorithms = {
        "BFS": bfs,
        "DFS": dfs,
        "UCS": ucs,
        "IDS": ids,
        "A* (Manhattan)": lambda s,g: astar_search(s, g, 'manhattan'),
        "A* (Misplaced)": lambda s,g: astar_search(s, g, 'misplaced'),
        "Hill Climbing": hill_climbing,
        "Hill Climbing (Restart)": hill_climbing_with_restart,
        "Genetic Algorithm": genetic_algorithm_search
    }
    
    all_results = {}
    
    # Test each algorithm
    for algo_name, algo_func in algorithms.items():
        print(f"\n{'='*40}")
        print(f"Analyzing: {algo_name}")
        print(f"{'='*40}")
        
        start_time = time.time()
        results = run_all_tests(algo_func, algo_name, selected_cases)
        total_time = time.time() - start_time
        
        all_results[algo_name] = results
        print(f"Total analysis time for {algo_name}: {total_time:.2f} seconds")
    
    # Generate comprehensive report
    print("\n" + "="*80)
    print("COMPREHENSIVE ANALYSIS REPORT")
    print("="*80)

    # For each selected test case
    for case_name in selected_cases:
        case_info = TEST_CASES[case_name]
        print(f"\n📊 Test Case: {case_name}")
        print(f"Description: {case_info['description']}")
        print(f"Optimal Solution: {case_info['optimal_length']} moves")
        print("-"*70)
        print(f"{'Algorithm':<25} {'Time (s)':<10} {'Nodes':<12} {'Path Len':<10} {'Found':<8}")
        print("-"*70)
#Abdelrhman Reda Abdelrhman Torad
        for algo_name in algorithms.keys():
            result = all_results[algo_name].get(case_name, {})
            time_taken = result.get('time_taken', 0)
            nodes = result.get('nodes_expanded', 'N/A')
            path_len = result.get('path_length', 'N/A')
            found = '✓' if result.get('solution_found', False) else '✗'

            print(f"{algo_name:<25} {time_taken:<10.4f} {nodes:<12} {path_len:<10} {found:<8}")

    # Summary statistics
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)

    successful_algorithms = {}
    for algo_name in algorithms.keys():
        success_count = sum(1 for case_name in selected_cases
                          if all_results[algo_name].get(case_name, {}).get('solution_found', False))
        successful_algorithms[algo_name] = success_count

    print(f"{'Algorithm':<25} {'Success Rate':<15} {'Avg Time (s)':<15}")
    print("-"*80)

    for algo_name, success_count in successful_algorithms.items():
        success_rate = f"{success_count}/{len(selected_cases)}"
        avg_time = sum(all_results[algo_name].get(case, {}).get('time_taken', 0)
                      for case in selected_cases) / len(selected_cases)

        print(f"{algo_name:<25} {success_rate:<15} {avg_time:<15.4f}")

    return all_results, selected_cases

def save_analysis_results(results, selected_cases, filename="report/analysis_results.txt"):
    """Save analysis results to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("8-Puzzle Algorithm Analysis Results\n")
        f.write("="*60 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for algo_name, algo_results in results.items():
            f.write(f"Algorithm: {algo_name}\n")
            f.write("-"*40 + "\n")

            for case_name in selected_cases:
                if case_name in algo_results:
                    result = algo_results[case_name]
                    case_info = TEST_CASES[case_name]
                    f.write(f"  Test Case: {case_name}\n")
                    f.write(f"    Description: {case_info['description']}\n")
                    f.write(f"    Optimal Length: {case_info['optimal_length']} moves\n")
                    f.write(f"    Solution Found: {'Yes' if result.get('solution_found') else 'No'}\n")

                    if result.get('solution_found'):
                        f.write(f"    Path Length: {result.get('path_length')} moves\n")
                        nodes = result.get('nodes_expanded', 'N/A')
                        if isinstance(nodes, int):
                            f.write(f"    Nodes Expanded: {nodes:,}\n")
                        else:
                            f.write(f"    Nodes Expanded: {nodes}\n")
                        f.write(f"    Time Taken: {result.get('time_taken', 0):.4f} seconds\n")

                    f.write("\n")

            f.write("\n")

    # Append recommendations
    append_recommendations(results, selected_cases, filename)

    print(f"✓ Results saved to {filename}")

def append_recommendations(results, selected_cases, filename):
    """Append recommendations to the analysis results file"""
    # Collect all successful results
    successful_results = []
    for algo_name, algo_results in results.items():
        for case_name in selected_cases:
            if case_name in algo_results:
                result = algo_results[case_name]
                if result.get('solution_found', False):
                    successful_results.append({
                        'algorithm': algo_name,
                        'time': result.get('time_taken', float('inf')),
                        'nodes': result.get('nodes_expanded', float('inf')) if isinstance(result.get('nodes_expanded'), int) else float('inf'),
                        'path_length': result.get('path_length', float('inf'))
                    })

    if not successful_results:
        return

    # Find fastest algorithm
    fastest = min(successful_results, key=lambda x: x['time'])
    fastest_algo = fastest['algorithm']
    fastest_time = fastest['time']

    # Find most efficient (least nodes)
    efficient_results = [r for r in successful_results if r['nodes'] != float('inf')]
    if efficient_results:
        most_efficient = min(efficient_results, key=lambda x: x['nodes'])
        efficient_algo = most_efficient['algorithm']
        efficient_nodes = most_efficient['nodes']
    else:
        efficient_algo = "N/A"
        efficient_nodes = "N/A"

    # Find shortest path
    shortest_path = min(successful_results, key=lambda x: x['path_length'])
    shortest_algo = shortest_path['algorithm']
    shortest_length = shortest_path['path_length']

    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\nRECOMMENDATIONS\n")
        f.write("-" * 40 + "\n")
        f.write(f"Fastest Algorithm: {fastest_algo} ({fastest_time:.4f}s)\n")
        if efficient_algo != "N/A":
            f.write(f"Most Efficient (Nodes): {efficient_algo} ({efficient_nodes} nodes)\n")
        else:
            f.write(f"Most Efficient (Nodes): {efficient_algo} ({efficient_nodes})\n")
        f.write(f"Shortest Path: {shortest_algo} ({shortest_length} moves)\n")

def save_csv_results(results, selected_cases, filename="report/comparison_table.csv"):
    """Save results in CSV format"""
    import csv

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        header = ['Algorithm', 'Test Case', 'Solution Found', 'Time (s)',
                  'Nodes Expanded', 'Path Length', 'Optimal Length']
        writer.writerow(header)

        # Write data
        for algo_name, algo_results in results.items():
            for case_name in selected_cases:
                if case_name in algo_results:
                    result = algo_results[case_name]
                    case_info = TEST_CASES[case_name]
                    row = [
                        algo_name,
                        case_name,
                        'Yes' if result.get('solution_found') else 'No',
                        f"{result.get('time_taken', 0):.4f}",
                        result.get('nodes_expanded', 'N/A'),
                        result.get('path_length', 'N/A'),
                        case_info['optimal_length']
                    ]
                    writer.writerow(row)

    print(f"✓ CSV results saved to {filename}")

if __name__ == "__main__":
    print("Starting comprehensive analysis...")
    all_results, selected_cases = comprehensive_analysis()

    # Save results
    save_analysis_results(all_results, selected_cases)
    save_csv_results(all_results, selected_cases)

    # Generate charts
    analyzer = PerformanceAnalyzer()

    # Add results to analyzer for all algorithms and test cases
    for algo_name, algo_results in all_results.items():
        for case_name in selected_cases:
            if case_name in algo_results:
                result = algo_results[case_name]
                if result.get('solution_found', False):
                    analyzer.add_result(algo_name, result)

    # Generate comparison chart
    comparison_path = analyzer.plot_comparison_chart()
    print(f"✓ Comparison chart saved to {comparison_path}")

    # Generate GA fitness chart (only if GA was successful)
    if 'Genetic Algorithm' in all_results:
        ga_results = all_results['Genetic Algorithm']
        for case_name in selected_cases:
            if case_name in ga_results and ga_results[case_name].get('solution_found', False):
                ga_result = ga_results[case_name]
                if 'fitness_history' in ga_result:
                    fitness_path = analyzer.plot_fitness_progress(ga_result)
                    if fitness_path:
                        print(f"✓ GA fitness chart saved to {fitness_path}")
                    break  # Only plot for first successful GA result

    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print(f"Results saved to 'report/' directory")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
