import numpy as np
import matplotlib.pyplot as plt


def eggholder(x):
    return -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0] / 2 + (x[1] + 47)))) - x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))


def holder_table(x):
    return -abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi)))


class Particle:
    def __init__(self, bounds):
        self.position = np.random.uniform(bounds[:, 0], bounds[:, 1])
        self.velocity = np.zeros_like(self.position)
        self.best_position = self.position.copy()


def pso_optimizer(objective_func, bounds, num_particles, num_iterations, inertia_weight, cognitive_weight, social_weight):
    num_dimensions = len(bounds)
    particles = [Particle(bounds) for _ in range(num_particles)]

    global_best_position = None
    global_best_fitness = np.inf
    fitness_history = []

    for iteration in range(num_iterations):
        for particle in particles:
            fitness = objective_func(particle.position)
            if fitness < objective_func(particle.best_position):
                particle.best_position = particle.position.copy()

            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = particle.position.copy()

            particle.velocity = (inertia_weight * particle.velocity +
                                 cognitive_weight * np.random.rand() * (particle.best_position - particle.position) +
                                 social_weight * np.random.rand() * (global_best_position - particle.position))
            particle.position += particle.velocity
            particle.position = np.clip(particle.position, bounds[:, 0], bounds[:, 1])

        fitness_history.append(global_best_fitness)

    return global_best_position, fitness_history


# Parameters
bounds = np.array([[-512, 512], [-512, 512]])
num_particles = 200
num_iterations = 200
inertia_weight = 0.5
cognitive_weight = 0.8
social_weight = 0.8

# Perform PSO optimization for Eggholder function
eggholder_best_solution, eggholder_fitness_history = pso_optimizer(eggholder, bounds, num_particles, num_iterations,
                                                                   inertia_weight, cognitive_weight, social_weight)

# Perform PSO optimization for Holder Table function
holder_table_best_solution, holder_table_fitness_history = pso_optimizer(holder_table, bounds, num_particles,
                                                                       num_iterations, inertia_weight, cognitive_weight,
                                                                       social_weight)

# Plotting the convergence history for Eggholder function
plt.figure(figsize=(8, 6))
plt.plot(range(num_iterations), eggholder_fitness_history)
plt.title('Convergence History - Eggholder Function')
plt.xlabel('Iteration')
plt.ylabel('Best Fitness')
plt.grid(True)
plt.show()

# Plotting the convergence history for Holder Table function
plt.figure(figsize=(8, 6))
plt.plot(range(num_iterations), holder_table_fitness_history)
plt.title('Convergence History - Holder Table Function')
plt.xlabel('Iteration')
plt.ylabel('Best Fitness')
plt.grid(True)
plt.show()

print("Best Solution - Eggholder Function:")
print(eggholder_best_solution)
print("Objective Value - Eggholder Function:")
print(eggholder(eggholder_best_solution))
print()
print("Best Solution - Holder Table Function:")
print(holder_table_best_solution)
print("Objective Value - Holder Table Function:")
print(holder_table(holder_table_best_solution))





