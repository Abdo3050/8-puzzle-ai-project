import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

class PerformanceAnalyzer:
    def __init__(self):
        self.results = {}
        self.comparison_data = []
    
    def add_result(self, algorithm_name, result):
        """Add algorithm result for analysis"""
        self.results[algorithm_name] = result
        
        metrics = {
            'Algorithm': algorithm_name,
            'Time (s)': result.get('time_taken', 0),
            'Nodes Expanded': result.get('nodes_expanded', 0),
            'Path Length': result.get('path_length', 0),
            'Solution Found': result.get('solution_found', False),
            'Optimal': True if algorithm_name in ['BFS', 'UCS', 'A*'] else False
        }
        
        if 'generations' in result:
            metrics['Generations'] = result['generations']
        if 'iterations' in result:
            metrics['Iterations'] = result['iterations']
        if 'final_h' in result:
            metrics['Final Heuristic'] = result['final_h']
        
        self.comparison_data.append(metrics)
    
    def generate_comparison_table(self):
        """Generate comparison table"""
        df = pd.DataFrame(self.comparison_data)
        
        columns_order = ['Algorithm', 'Solution Found', 'Time (s)', 'Nodes Expanded', 
                        'Path Length', 'Optimal']
        additional_cols = [col for col in df.columns if col not in columns_order]
        
        df = df[columns_order + additional_cols]
        pd.set_option('display.float_format', '{:.4f}'.format)
        
        return df
    
    def plot_comparison_chart(self, save_path='report/comparison_chart.png'):
        """Create visualization charts"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        algorithms = [r['Algorithm'] for r in self.comparison_data]
        times = [r['Time (s)'] for r in self.comparison_data]
        nodes = [r['Nodes Expanded'] for r in self.comparison_data]
        path_lengths = [r['Path Length'] if r['Path Length'] != 0 else 1 for r in self.comparison_data]
        found = [1 if r['Solution Found'] else 0 for r in self.comparison_data]
        
        # 1. Time comparison
        axes[0, 0].bar(algorithms, times, color='skyblue')
        axes[0, 0].set_title('Execution Time Comparison')
        axes[0, 0].set_ylabel('Time (seconds)')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # 2. Nodes expanded
        axes[0, 1].bar(algorithms, nodes, color='lightgreen')
        axes[0, 1].set_title('Nodes Expanded Comparison')
        axes[0, 1].set_ylabel('Number of Nodes')
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # 3. Path length
        axes[1, 0].bar(algorithms, path_lengths, color='lightcoral')
        axes[1, 0].set_title('Path Length Comparison')
        axes[1, 0].set_ylabel('Path Length (moves)')
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 4. Success rate
        axes[1, 1].bar(algorithms, found, color='gold')
        axes[1, 1].set_title('Solution Found (1=Yes, 0=No)')
        axes[1, 1].set_ylabel('Success')
        axes[1, 1].set_ylim([0, 1.2])
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def plot_fitness_progress(self, ga_result, save_path='report/ga_fitness.png'):
        """Plot GA fitness progress"""
        if 'fitness_history' not in ga_result:
            return None
        
        fitness_history = ga_result['fitness_history']
        
        plt.figure(figsize=(10, 6))
        plt.plot(fitness_history, label='Best Fitness', linewidth=2)
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.title('Genetic Algorithm Fitness Progress')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        if fitness_history:
            plt.axhline(y=fitness_history[-1], color='r', linestyle='--', alpha=0.5,
                       label=f'Final Fitness: {fitness_history[-1]:.4f}')
        
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def generate_report_text(self):
        """Generate detailed text report"""
        report = []
        report.append("=" * 70)
        report.append("8-PUZZLE AI ALGORITHMS PERFORMANCE REPORT")
        report.append("=" * 70)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("\n")
        
        total_algorithms = len(self.results)
        successful_algorithms = sum(1 for r in self.comparison_data if r['Solution Found'])
        
        report.append("SUMMARY")
        report.append("-" * 40)
        report.append(f"Total Algorithms Tested: {total_algorithms}")
        report.append(f"Successful Algorithms: {successful_algorithms}")
        report.append(f"Success Rate: {(successful_algorithms/total_algorithms)*100:.1f}%")
        report.append("\n")
        
        report.append("DETAILED ANALYSIS")
        report.append("-" * 40)
        
        for algo_name, result in self.results.items():
            report.append(f"\n{algo_name}:")
            report.append(f"  Solution Found: {'✓' if result.get('solution_found', False) else '✗'}")
            
            if result.get('solution_found', False):
                report.append(f"  Path Length: {result.get('path_length', 'N/A')}")
                nodes = result.get('nodes_expanded', 'N/A')
                if isinstance(nodes, int):
                    report.append(f"  Nodes Expanded: {nodes:,}")
                else:
                    report.append(f"  Nodes Expanded: {nodes}")
                report.append(f"  Time Taken: {result.get('time_taken', 0):.4f} seconds")
            
            if 'generations' in result:
                report.append(f"  Generations: {result['generations']}")
            if 'iterations' in result:
                report.append(f"  Iterations: {result['iterations']}")
            if 'distance_to_goal' in result:
                report.append(f"  Distance to Goal: {result['distance_to_goal']}")
        
        report.append("\nRECOMMENDATIONS")
        report.append("-" * 40)
        
        successful = [r for r in self.comparison_data if r['Solution Found']]
        
        if successful:
            fastest = min(successful, key=lambda x: x['Time (s)'])
            most_efficient = min(successful, key=lambda x: x['Nodes Expanded'])
            shortest_path = min(successful, key=lambda x: x['Path Length'])
            
            report.append(f"Fastest Algorithm: {fastest['Algorithm']} ({fastest['Time (s)']:.4f}s)")
            report.append(f"Most Efficient (Nodes): {most_efficient['Algorithm']} ({most_efficient['Nodes Expanded']:,} nodes)")
            report.append(f"Shortest Path: {shortest_path['Algorithm']} ({shortest_path['Path Length']} moves)")
            
            if fastest['Algorithm'] == 'A* (Manhattan)':
                report.append("\nOverall Recommendation: A* with Manhattan Distance")
                report.append("  - Guaranteed optimal solution")
                report.append("  - Fast execution time")
                report.append("  - Memory efficient")
        
        report.append("\n" + "=" * 70)
        
        return '\n'.join(report)
    
    def save_report(self, output_file='report/final_report.txt'):
        """Save complete report to file"""
        report_text = self.generate_report_text()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        df = self.generate_comparison_table()
        df.to_csv('report/comparison_table.csv', index=False)
        
        return output_file
