import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time

def calculate_fitness(individual, target):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == target[i]:
            fitness += 1
    return fitness

def generate_population(size, length, goal):
    population = []
    for i in range(size):
        population.append([])
        for j in range(length):
            population[i].append(random.choice(goal))
    return population

def mutate(individual, goal):
    mutation_point = random.randint(0, len(individual) - 1)
    individual[mutation_point] = random.choice(goal)

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def select_parents(population, fitnesses):
    parents = []
    sum_fitness = sum(fitnesses)
    for i in range(2):
        rand = random.uniform(0, sum_fitness)
        for j, fitness in enumerate(fitnesses):
            if rand < fitness:
                parents.append(population[j])
                break
            rand -= fitness
    return parents

def new_generation(old_population, goal, mutation_rate, crossover_rate):
    population_size = len(old_population)
    population_length = len(old_population[0])
    fitnesses = [0] * population_size
    for i in range(population_size):
        fitnesses[i] = calculate_fitness(old_population[i], goal)
    new_population = []
    for i in range(population_size):
        parents = select_parents(old_population, fitnesses)
        child = crossover(parents[0], parents[1])
        if random.random() < mutation_rate:
            mutate(child, goal)
        new_population.append(child)
    return new_population

def run_evolution(population, goal, mutation_rate, crossover_rate, max_generations):
    for generation in range(max_generations):
        print("Generation {}:".format(generation))
        print(population)
        population = new_generation(population, goal, mutation_rate, crossover_rate)
        if goal in population:
            print("Solution found in generation {}!".format(generation))
            break
    return population

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Genetic Algorithms")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    size_entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
    size_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
    
    mutation_rate_entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
    mutation_rate_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
    
    crossover_rate_entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
    crossover_rate_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))
    
    max_generations_entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
    max_generations_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))
    
    goal_entry = ttk.Entry(mainframe, width=7, textvariable=tk.StringVar())
    goal_entry.grid(column=2, row=5, sticky=(tk.W, tk.E))
    
    ttk.Button(mainframe, text="Run", command=lambda: run_evolution(
        generate_population(int(size_entry.get()), len(goal_entry.get()), goal_entry.get()), 
        goal_entry.get(), 
        float(mutation_rate_entry.get()), 
        float(crossover_rate_entry.get()), 
        int(max_generations_entry.get())
        )).grid(column=3, row=5, sticky=tk.W)
    
    ttk.Label(mainframe, text="Population size:").grid(column=1, row=1, sticky=tk.E)
    ttk.Label(mainframe, text="Mutation rate:").grid(column=1, row=2, sticky=tk.E)
    ttk.Label(mainframe, text="Crossover rate:").grid(column=1, row=3, sticky=tk.E)
    ttk.Label(mainframe, text="Max generations:").grid(column=1, row=4, sticky=tk.E)
    ttk.Label(mainframe, text="Goal:").grid(column=1, row=5, sticky=tk.E)
    
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    size_entry.focus()
    root.bind('<Return>', lambda event: run_evolution(
        generate_population(int(size_entry.get()), len(goal_entry.get()), goal_entry.get()), 
        goal_entry.get(), 
        float(mutation_rate_entry.get()), 
        float(crossover_rate_entry.get()), 
        int(max_generations_entry.get())
        ))
    root.mainloop()