import numpy as np
import matplotlib.pyplot as plt

def eggholder(x, y):
    return -(y + 47) * np.sin(np.sqrt(abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(abs(x - (y + 47))))

def holder_table(x, y):
    return -abs(np.sin(x) * np.cos(y) * np.exp(abs(1 - np.sqrt(x ** 2 + y ** 2) / np.pi)))

def de_optimization(objective_func, bounds, pop_size, max_gens, crossover_prob, K, F):
    num_params = len(bounds)
    min_bound, max_bound = np.asarray(bounds).T

    def is_valid(candidate):
        return np.all(candidate >= min_bound) and np.all(candidate <= max_bound)

    population = np.random.uniform(min_bound, max_bound, size=(pop_size, num_params))
    best_fitness = np.inf
    best_candidate = None
    convergence_history = []

    if pop_size < 3:
        raise ValueError("Population size must be greater than or equal to 3")

    for gen in range(max_gens):
        mutant_vectors = []
        for i in range(pop_size):
            indices = np.arange(pop_size)
            indices = np.delete(indices, i)
            indices = indices.astype(int)
            random_indices = np.random.choice(indices, size=3, replace=False)
            a, b, c = population[random_indices[0]], population[random_indices[1]], population[random_indices[2]]
            mutant_vector = np.clip(a + F * (b - c), min_bound, max_bound)
            mutant_vectors.append(mutant_vector)

        trial_vectors = []
        for i in range(pop_size):
            trial_vector = population[i].copy()
            for j in range(num_params):
                if np.random.rand() < crossover_prob:
                    trial_vector[j] = mutant_vectors[i][j]
            trial_vectors.append(trial_vector)

        fitness_values = np.array([objective_func(*candidate) for candidate in trial_vectors])
        for i in range(pop_size):
            if fitness_values[i] < best_fitness and is_valid(trial_vectors[i]):
                best_fitness = fitness_values[i]
                best_candidate = trial_vectors[i]

        population = trial_vectors
        convergence_history.append(best_fitness)

    return best_candidate, convergence_history

eggholder_bounds = [(-512, 512), (-512, 512)]
pop_size = 20
max_gens = 50
crossover_prob = 0.8
K = 0.5
F = np.random.uniform(-2, 2)
best_eggholder, eggholder_convergence = de_optimization(eggholder, eggholder_bounds, pop_size, max_gens, crossover_prob,
                                                       K, F)
plt.plot(eggholder_convergence)
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Convergence History - Eggholder Function")
plt.show()

holder_table_bounds = [(-10, 10), (-10, 10)]
pop_size = 200
max_gens = 200
crossover_prob = 0.8
K = 0.5
F = np.random.uniform(-2, 2)
best_holder_table, holder_table_convergence = de_optimization(holder_table, holder_table_bounds, pop_size, max_gens,
                                                             crossover_prob, K, F)
plt.plot(holder_table_convergence)
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Convergence History - Holder Table Function")
plt.show()

print("Best Eggholder Candidate:", best_eggholder)
print("Eggholder Objective Value:", eggholder(*best_eggholder))

print("Best Holder Table Candidate:", best_holder_table)
print("Holder Table Objective Value:", holder_table(*best_holder_table))

