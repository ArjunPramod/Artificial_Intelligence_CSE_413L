# AP21110010192

import random

cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 1),
    'D': (3, 6),
    'E': (4, 2),
    'F': (5, 5),
    'G': (6, 0),
    'H': (7, 4)
}

def initial_population(population_size):
    population = []
    for _ in range(population_size):
        route = list(cities.keys())
        random.shuffle(route)
        population.append(route)
    return population

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += distance_between_cities(cities[city1], cities[city2])
    return total_distance

def distance_between_cities(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def select_parents(population):
    parent1, parent2 = random.sample(population, 2)
    return parent1, parent2

def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 2)
    end = random.randint(start + 1, len(parent1) - 1)
    child = [None] * len(parent1)
    for i in range(start, end + 1):
        child[i] = parent1[i]
    remaining_cities = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(child)):
        if child[i] is None:
            child[i] = remaining_cities[j]
            j += 1
    return child

def mutate(route):
    index1, index2 = random.sample(range(len(route)), 2)
    route[index1], route[index2] = route[index2], route[index1]

def genetic_algorithm(num_generations, population_size):
    population = initial_population(population_size)
    for generation in range(num_generations):
        population = sorted(population, key=lambda x: calculate_total_distance(x))
        best_route = population[0]
        print(f"Generation {generation}: Best distance = {calculate_total_distance(best_route)}")
        new_population = [best_route]

        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            if random.random() < 0.2:
                mutate(child)
            new_population.append(child)

        population = new_population

    return population[0]

if __name__ == "__main__":
    num_generations = 100
    population_size = 50
    best_route = genetic_algorithm(num_generations, population_size)
    print("Best Route:", best_route)
    print("Best Distance:", calculate_total_distance(best_route))
