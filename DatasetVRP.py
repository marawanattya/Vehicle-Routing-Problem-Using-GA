import json
import numpy as np
import random
from collections import deque

# Parameters
POPULATION_SIZE = 200
NUM_GENERATIONS = 20
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.8
TOURNAMENT_SIZE = 5
VEHICLE_CAPACITY = 15

# Load data from JSON file
def load_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    depot = tuple(data["depot"])
    deliveries = [tuple(coord) for coord in data["deliveries"]]
    demands = data["demands"]
    num_vehicles = data["num_vehicles"]
    return depot, deliveries, demands, num_vehicles

# Helper functions
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Fitness function
def fitness(chromosome):
    total_distance = 0
    for route in chromosome:
        load = 0
        route_distance = 0
        prev_location = DEPOT
        for customer in route:
            route_distance += euclidean_distance(prev_location, DELIVERIES[customer])
            load += DEMANDS[customer]
            if load > VEHICLE_CAPACITY:
                # Penalty for exceeding capacity
                route_distance += 1e6
            prev_location = DELIVERIES[customer]
        route_distance += euclidean_distance(prev_location, DEPOT)  # Return to depot
        total_distance += route_distance
    return total_distance

# Create initial population
def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        deliveries = list(range(len(DELIVERIES)))
        random.shuffle(deliveries)
        routes = []
        while deliveries:
            route = []
            load = 0
            for i in list(deliveries):
                if load + DEMANDS[i] <= VEHICLE_CAPACITY:
                    route.append(i)
                    load += DEMANDS[i]
                    deliveries.remove(i)
            routes.append(route)
        population.append(routes)
    return population

# Tournament selection
def tournament_selection(population, fitnesses):
    candidates = random.sample(range(len(population)), TOURNAMENT_SIZE)
    best = min(candidates, key=lambda idx: fitnesses[idx])
    return population[best]

# Order crossover for VRP
def crossover(parent1, parent2):
    child = []
    for route1, route2 in zip(parent1, parent2):
        size = len(route1)
        if size < 2:
            child.append(route1)
            continue
        start, end = sorted(random.sample(range(size), 2))
        fragment = route1[start:end]

        # Ensure `new_route` starts with all genes from `route2`
        new_route = deque([gene for gene in route2 if gene not in fragment])
        for gene in fragment:
            if gene in new_route:
                new_route.remove(gene)

        # Rotate the remaining genes to align with the fragment's start
        new_route.rotate(-start)
        child_route = list(fragment) + list(new_route)[:size - len(fragment)]
        child.append(child_route)

    return child


# Swap mutation
def mutate(chromosome):
    for route in chromosome:
        if len(route) < 2:
            continue  # Skip mutation for routes with fewer than 2 customers
        if random.random() < MUTATION_RATE:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]

# Main GA loop
def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_fitness = float('inf')

    for generation in range(NUM_GENERATIONS):
        fitnesses = [fitness(chromosome) for chromosome in population]
        new_population = []

        # Keep the elite (top solutions)
        elite_size = max(1, POPULATION_SIZE // 10)
        elite_indices = np.argsort(fitnesses)[:elite_size]
        elite = [population[idx] for idx in elite_indices]
        new_population.extend(elite)

        # Generate new offspring
        while len(new_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            if random.random() < CROSSOVER_RATE:
                child = crossover(parent1, parent2)
            else:
                child = parent1
            mutate(child)
            new_population.append(child)

        # Update population
        population = new_population

        # Update best solution
        current_best_idx = np.argmin(fitnesses)
        current_best = population[current_best_idx]
        current_best_fitness = fitnesses[current_best_idx]
        if current_best_fitness < best_fitness:
            best_solution = current_best
            best_fitness = current_best_fitness

        # Progress output
        if generation % 500 == 0 or generation == NUM_GENERATIONS - 1:
            print(f"Generation {generation}, Best Distance: {best_fitness}")

    return best_solution, best_fitness

# Load data and run the algorithm
DEPOT, DELIVERIES, DEMANDS, NUM_VEHICLES = load_data("vrp_data.json")
best_solution, best_distance = genetic_algorithm()
print("\nBest Solution:")
for route in best_solution:
    print("Route:", [DEPOT] + [DELIVERIES[customer] for customer in route] + [DEPOT])
print(f"Total Distance: {best_distance}")
