'''Jallah Kollie
   Juan DelaPuente
final program 1, May 13, 2025

Our termination condition is 100

For the size of my swarm, I used 8 at first in which after running it one time seem to work but
running it again, I saw the results were far from what I wanted. So I used 5000 as Dr. Rauff suggested and my
results became more consistent. I used 100 iterations. 


'''


import numpy as np
import random
import matplotlib.pyplot as plt
def poly(coeffs, x):
    return coeffs[0]*x**3 + coeffs[1]*x**2 + coeffs[2]*x + coeffs[3]

def make_objective(x_vals, y_vals):
    def objective(coeffs):
        #loop through x-vals and use current coef to get predicted y_vals
        predictions = [poly(coeffs, x) for x in x_vals]
        # Compute mean squared error
        mse = np.mean([(y_hat - y_true)**2 for y_hat, y_true in zip(predictions, y_vals)])
        return mse
    return objective

class Particle:
    def __init__(self, dim):
        self.pos = np.random.uniform(-5, 5, dim)
        self.vel = np.zeros(dim)
        self.best = self.pos.copy()

    def update_best(self, obj_func):
        if obj_func(self.pos) < obj_func(self.best):
            self.best = self.pos.copy()

    def move(self, global_best, alpha=1.5, beta=1.5):
        for i in range(len(self.pos)):
            r1, r2 = random.random(), random.random()
            self.vel[i] += alpha * r1 * (global_best[i] - self.best[i]) + beta * r2 * (self.best[i] - self.pos[i])
            self.pos[i] += self.vel[i]
            self.pos[i] = max(-5, min(5, self.pos[i]))

def pso(obj_func, dim=4, num_particles=5000, max_iter=100):
    particles = [Particle(dim) for _ in range(num_particles)]
    global_best = min(particles, key=lambda p: obj_func(p.pos)).pos.copy()

    for _ in range(max_iter):
        for p in particles:
            p.move(global_best)
            p.update_best(obj_func)
        best_particle = min(particles, key=lambda p: obj_func(p.best))
        if obj_func(best_particle.best) < obj_func(global_best):
            global_best = best_particle.best.copy()

    return global_best, obj_func(global_best)

# Example data
x_vals = [0, .73, 1.33, 2.09, 2.1, 2.38, 3.28, 3.50]
y_vals = [2.00, 1.46, 0.94, 0.84, 0.85, 1.12, 3.73, 4.88]

# Create objective function
objective = make_objective(x_vals, y_vals)

# Run PSO to minimize the error
best_pos, best_val = pso(objective)

# Output results
print("Best polynomial coefficients: ", best_pos)
#print("Final MSE:", best_val)

y_pred = [poly(best_pos,x) for x in x_vals]

y_pred = [poly(best_pos, x) for x in x_vals]

# Average absolute difference
abs_diff = np.mean([abs(y - y_hat) for y, y_hat in zip(y_vals, y_pred)])
print("\nAverage absolute difference:", abs_diff)

    
    
plt.scatter(x_vals, y_vals, label='Data', color = 'red')

plt.plot(x_vals, y_pred, label='Fitted Polynomial', color='blue')

plt.legend()
plt.show()
