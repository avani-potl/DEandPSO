# DEandPSO
Developed Python programs to implement Differential Evolution (DE) and Particle Swarm Optimization (PSO) techniques for solving single-objective optimization problems. Applied DE and PSO to Eggholder and Holder Table functions, achieving convergence trends through systematic experimentation. 
**DIFFERENTIAL EVOLUTION**
The code begins by importing necessary libraries: numpy for numerical operations and matplotlib.pyplot for visualization. The objective functions, eggholder and holder_table, are defined. These functions represent the mathematical expressions for the Eggholder and Holder Table functions, respectively. The DE optimization process is implemented through the de_optimization function.

DE Optimization
Initialization: The optimization process starts by defining the search space bounds for each function (eggholder_bounds and holder_table_bounds). The population size (pop_size), maximum generations (max_gens), crossover probability (crossover_prob), and DE parameters K and F are set.

Main Loop: The DE optimization algorithm iterates over multiple generations. Within each generation, the algorithm generates mutant vectors by combining three randomly selected candidate vectors. The trial vectors are then formed by applying crossover to the current population and the mutant vectors. The fitness values of the trial vectors are computed using the respective objective functions.

Selection: For each candidate in the population, if the fitness of its trial vector is better than the best fitness so far and the trial vector is within the defined bounds, the best fitness is updated, and the best candidate is set to the trial vector.

Update Population: The population is updated with the trial vectors, and the best fitness value for the current generation is recorded in the convergence_history.

Optimization Process for Eggholder Function
For the Eggholder function:

Search space bounds: (-512, 512) for both x and y coordinates
Population size: 20
Maximum generations: 50
Crossover probability: 0.8
DE parameters: K = 0.5, F = random value between -2 and 2
The convergence history is plotted to visualize the optimization progress. After the optimization is complete, the best candidate and its corresponding objective value are printed.

Optimization Process for Holder Table Function
For the Holder Table function:

Search space bounds: (-10, 10) for both x and y coordinates
Population size: 200
Maximum generations: 200
Crossover probability: 0.8
DE parameters: K = 0.5, F = random value between -2 and 2
Similarly, the convergence history is plotted for the Holder Table function, and the best candidate along with its objective value are printed.


<img width="307" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/f2af601b-6e66-4c37-8093-ec7ddf40ba68">
<img width="347" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/9448af40-2747-406b-b01e-45caed04d56b">
<img width="308" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/6cf37ca0-7162-458d-b4df-6593b45a2dd1">
<img width="382" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/7f0b66ca-1a8e-4046-b477-d11db4c4dd7b">
<img width="316" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/1831fbc6-1d3f-4452-b1bf-9f61bda8919d">
<img width="330" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/64655751-151d-4958-83bc-023c10bf312a">



**PARTICLE SWARM OPTIMIZATION**

The code starts by importing the necessary libraries: numpy for numerical operations and matplotlib.pyplot for data visualization. The objective functions, eggholder and holder_table, are defined to express the mathematical expressions for the Eggholder and Holder Table functions, respectively. The PSO optimization process is implemented using the Particle class and the pso_optimizer function.

PSO Optimization
Particle Initialization: The optimization process commences with defining the search space bounds for each function (bounds). The number of particles (num_particles), the maximum number of iterations (num_iterations), and the weights for different aspects of particle movement (inertia_weight, cognitive_weight, and social_weight) are set.

Particle Class: A Particle class is defined to encapsulate the behavior of a particle in the optimization process. Each particle has a position and velocity, both of which are initialized randomly within the defined bounds. The particle's best position (personal best) is initially set to its current position.

Main PSO Loop: The PSO algorithm iterates through multiple iterations. Within each iteration, each particle's fitness is evaluated using the objective function. If the particle's current position yields a better fitness than its previous best, the best position is updated. Similarly, if a particle discovers a position with better fitness than the global best, both the global best fitness and position are updated.

Update Particle State: The particle's velocity is updated using a combination of its current velocity, cognitive influence (personal best), and social influence (global best). This updated velocity is used to adjust the particle's position. The position is then clipped to ensure it remains within the defined bounds.

Convergence Tracking: The history of the global best fitness values is recorded in the fitness_history list, allowing visualization of convergence over iterations.

Optimization Process for Eggholder Function
For the Eggholder function:

Search space bounds: (-512, 512) for both x and y coordinates
Number of particles: 200
Number of iterations: 200
Inertia weight: 0.5
Cognitive weight: 0.8
Social weight: 0.8
The convergence history is plotted to visualize the optimization progress. The best solution candidate and its corresponding objective value are printed.

Optimization Process for Holder Table Function
For the Holder Table function:

Search space bounds: (-512, 512) for both x and y coordinates
Number of particles: 200
Number of iterations: 200
Inertia weight: 0.5
Cognitive weight: 0.8
Social weight: 0.8
Similarly, the convergence history is plotted for the Holder Table function, and the best solution candidate along with its objective value are printed.

<img width="329" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/f521e7f5-7a30-44c6-9059-af5980159edc">
<img width="302" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/d99c99fc-bed0-4603-8c4b-7e99cb4c9bff">
<img width="268" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/49a09777-8448-407f-ba9d-64ec0a2345b5">
<img width="281" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/6b02a005-d58d-41b9-9d9b-41031de05a45">
<img width="306" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/e41b5dce-5108-4686-867d-6ed82d23fe1a">
<img width="290" alt="image" src="https://github.com/avani-potl/DEandPSO/assets/137739877/d7942ac9-3565-4dfc-8bac-cfc812eeb8df">

