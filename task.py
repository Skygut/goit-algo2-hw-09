import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dimensions = len(bounds)
    current_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)
    ]
    current_value = func(current_solution)

    for _ in range(iterations):
        neighbor = [
            current_solution[i] + random.uniform(-epsilon, epsilon)
            for i in range(dimensions)
        ]
        # Перевірка меж
        neighbor = [
            max(bounds[i][0], min(bounds[i][1], neighbor[i])) for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

        if current_value < epsilon:
            break

    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dimensions = len(bounds)
    best_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)
    ]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [
            random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)
        ]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if best_value < epsilon:
            break

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    dimensions = len(bounds)
    current_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimensions)
    ]
    current_value = func(current_solution)

    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break

        neighbor = [
            current_solution[i] + random.uniform(-temp, temp) for i in range(dimensions)
        ]
        # Перевірка меж
        neighbor = [
            max(bounds[i][0], min(bounds[i][1], neighbor[i])) for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_solution, current_value = neighbor, neighbor_value

        if current_value < epsilon:
            break

    return current_solution, current_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
