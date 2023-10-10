# AP21110010192

import random

cities = {
    'A': (0, 0),
    'B': (2, 4),
    'C': (5, 2),
    'D': (7, 5),
    'E': (2, 7),
    'F': (8, 8),
    'G': (9, 6),
    'H': (3, 3)
}

def total_distance(tour):
    distance = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance += ((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2) ** 0.5
    return distance

def initial_population(pop_size):
    population = []
    cities_list = list(cities.keys())
    for _ in range(pop_size):
        random.shuffle(cities_list)
        population.append(cities_list[:])
    return population

def selection(population, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, 3)
        tournament.sort(key=lambda x: total_distance(x))
        selected_parents.append(tournament[0])
    return selected_parents

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [''] * len(parent1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining_cities = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(child)):
        if child[i] == '':
            child[i] = remaining_cities[j]
            j += 1
    return child

def mutation(child):
    idx1, idx2 = random.sample(range(len(child)), 2)
    child[idx1], child[idx2] = child[idx2], child[idx1]
    return child

population_size = 100
num_generations = 1000
num_parents = 50

population = initial_population(population_size)
for generation in range(num_generations):
    parents = selection(population, num_parents)
    new_population = parents.copy()
    
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        child = crossover(parent1, parent2)
        if random.random() < 0.2:  # Apply mutation with a low probability
            child = mutation(child)
        new_population.append(child)
    
    population = new_population


if __name__ == "__main__":
    best_tour = min(population, key=lambda x: total_distance(x))
    print("Best Tour:", best_tour)
    print("Total Distance:", total_distance(best_tour))
