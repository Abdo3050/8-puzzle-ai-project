import random
import numpy as np
from utils.state import PuzzleState
from utils.heuristics import manhattan_distance

class GeneticAlgorithm:
    def __init__(self, goal_board, population_size=100, max_generations=500,
                 mutation_rate=0.1, crossover_rate=0.8):
        self.goal_board = goal_board
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        
        # Flatten goal board for easier comparison
        self.goal_flat = [cell for row in goal_board for cell in row]
        
        # Statistics tracking
        self.best_fitness_history = []
        self.avg_fitness_history = []
    
    def create_chromosome(self):
        """Create a random chromosome (solution representation)"""
        moves = ['Up', 'Down', 'Left', 'Right']
        chromosome_length = random.randint(10, 50)
        return [random.choice(moves) for _ in range(chromosome_length)]
    
    def chromosome_to_state(self, chromosome, start_board):
        """Convert chromosome (move sequence) to final state"""
        current_board = [row[:] for row in start_board]
        
        for move in chromosome:
            # Find blank position
            blank_pos = None
            for i in range(3):
                for j in range(3):
                    if current_board[i][j] == 0:
                        blank_pos = (i, j)
                        break
                if blank_pos:
                    break
            
            if not blank_pos:
                break
            
            i, j = blank_pos
            
            # Apply move if valid
            if move == 'Up' and i > 0:
                current_board[i][j], current_board[i-1][j] = current_board[i-1][j], current_board[i][j]
            elif move == 'Down' and i < 2:
                current_board[i][j], current_board[i+1][j] = current_board[i+1][j], current_board[i][j]
            elif move == 'Left' and j > 0:
                current_board[i][j], current_board[i][j-1] = current_board[i][j-1], current_board[i][j]
            elif move == 'Right' and j < 2:
                current_board[i][j], current_board[i][j+1] = current_board[i][j+1], current_board[i][j]
        
        return PuzzleState(current_board)
    
    def fitness_function(self, chromosome, start_board):
        """Calculate fitness of a chromosome"""
        state = self.chromosome_to_state(chromosome, start_board)
        
        # Calculate Manhattan distance (lower is better)
        distance = manhattan_distance(state, self.goal_board)
        
        # Convert to fitness (higher is better)
        fitness = 1.0 / (distance + 1)
        
        # Bonus for shorter chromosomes
        length_penalty = len(chromosome) * 0.01
        fitness -= length_penalty
        
        return max(fitness, 0.001)
    
    def create_initial_population(self, start_board):
        """Create initial random population"""
        population = []
        for _ in range(self.population_size):
            chromosome = self.create_chromosome()
            fitness = self.fitness_function(chromosome, start_board)
            population.append((chromosome, fitness))
        
        return population
    
    def selection(self, population):
        """Select parents using tournament selection"""
        tournament_size = 3
        selected = []
        
        for _ in range(2):  # Select 2 parents
            tournament = random.sample(population, tournament_size)
            tournament.sort(key=lambda x: x[1], reverse=True)
            selected.append(tournament[0][0])
        
        return selected
    
    def crossover(self, parent1, parent2):
        """Perform single-point crossover"""
        if random.random() > self.crossover_rate:
            return parent1[:], parent2[:]
        
        min_len = min(len(parent1), len(parent2))
        if min_len <= 1:
            return parent1[:], parent2[:]
        
        crossover_point = random.randint(1, min_len - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        
        return child1, child2
    
    def mutation(self, chromosome):
        """Apply mutation to chromosome"""
        mutated = chromosome[:]
        moves = ['Up', 'Down', 'Left', 'Right']

        i = 0
        while i < len(mutated):
            if random.random() < self.mutation_rate:
                mutated[i] = random.choice(moves)

            if random.random() < self.mutation_rate / 2:
                if random.random() < 0.5 and len(mutated) < 100:
                    insert_pos = random.randint(0, len(mutated))
                    mutated.insert(insert_pos, random.choice(moves))
                    if insert_pos <= i:
                        i += 1
                elif len(mutated) > 5:
                    remove_pos = random.randint(0, len(mutated) - 1)
                    mutated.pop(remove_pos)
                    if remove_pos <= i:
                        i -= 1
            i += 1

        return mutated
    
    def run(self, start_board):
        """Main GA execution"""
        population = self.create_initial_population(start_board)
        nodes_expanded = len(population)  # Initial population count
        
        for generation in range(self.max_generations):
            population.sort(key=lambda x: x[1], reverse=True)
            
            best_fitness = population[0][1]
            avg_fitness = sum(f for _, f in population) / len(population)
            self.best_fitness_history.append(best_fitness)
            self.avg_fitness_history.append(avg_fitness)
            
            best_chromosome = population[0][0]
            best_state = self.chromosome_to_state(best_chromosome, start_board)
            
            if best_state.board == self.goal_board:
                return {
                    "solution_found": True,
                    "solution": best_chromosome,
                    "generations": generation + 1,
                    "best_fitness": best_fitness,
                    "path_length": len(best_chromosome),
                    "fitness_history": self.best_fitness_history
                }
            
            new_population = []
            elite_size = max(1, self.population_size // 10)
            new_population.extend(population[:elite_size])
            
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection(population)
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                
                fitness1 = self.fitness_function(child1, start_board)
                fitness2 = self.fitness_function(child2, start_board)
                
                new_population.append((child1, fitness1))
                if len(new_population) < self.population_size:
                    new_population.append((child2, fitness2))
            
            population = new_population
        
        population.sort(key=lambda x: x[1], reverse=True)
        best_chromosome = population[0][0]
        best_state = self.chromosome_to_state(best_chromosome, start_board)
        
        return {
            "solution_found": best_state.board == self.goal_board,
            "solution": best_chromosome,
            "generations": self.max_generations,
            "best_fitness": population[0][1],
            "final_state": best_state.board,
            "distance_to_goal": manhattan_distance(best_state, self.goal_board),
            "nodes_expanded": nodes_expanded,
            "fitness_history": self.best_fitness_history
        }

def genetic_algorithm_search(start_board, goal_board):
    """Wrapper function for Genetic Algorithm"""
    ga = GeneticAlgorithm(
        goal_board=goal_board,
        population_size=50,
        max_generations=100,
        mutation_rate=0.15,
        crossover_rate=0.7
    )
    
    result = ga.run(start_board)
    
    if result["solution_found"]:
        path = []
        current_board = [row[:] for row in start_board]
        
        for move in result["solution"]:
            path.append((move, [row[:] for row in current_board]))
            
            blank_pos = None
            for i in range(3):
                for j in range(3):
                    if current_board[i][j] == 0:
                        blank_pos = (i, j)
                        break
                if blank_pos:
                    break
            
            i, j = blank_pos
            
            if move == 'Up' and i > 0:
                current_board[i][j], current_board[i-1][j] = current_board[i-1][j], current_board[i][j]
            elif move == 'Down' and i < 2:
                current_board[i][j], current_board[i+1][j] = current_board[i+1][j], current_board[i][j]
            elif move == 'Left' and j > 0:
                current_board[i][j], current_board[i][j-1] = current_board[i][j-1], current_board[i][j]
            elif move == 'Right' and j < 2:
                current_board[i][j], current_board[i][j+1] = current_board[i][j+1], current_board[i][j]
        
        result["path"] = path
        result["path_length"] = len(path)
    
    return result
