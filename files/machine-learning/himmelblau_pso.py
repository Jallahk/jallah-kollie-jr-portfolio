'''Jallah Kollie particle swarming, 5/6/2025'''
import numpy as np
import random

#function
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

class Particle:
    def __init__(self, dim):
        self.dim = dim
        self.pos = np.random.uniform(0, 5, dim)
        self.vel = np.zeros(dim)
        self.best = self.pos.copy()

    def update_best(self, obj_func):
        if obj_func(self.pos) < obj_func(self.best):
            self.best = self.pos.copy()

    def move(self, global_best, alpha=1.5, beta=1.5):
        for i in range(self.dim):
            epsilon1 = random.random()
            epsilon2 = random.random()
            self.vel[i] += alpha * epsilon1 * (global_best[i] - self.best[i]) + \
                           beta * epsilon2 * (self.best[i] - self.pos[i])
            self.pos[i] += self.vel[i]
            self.pos[i] = max(0, min(5, self.pos[i]))


def pso(obj_func, dim=2, num_particles=30, max_iter=100):
    # Initialize particles
    particles = [Particle(dim) for _ in range(num_particles)]
    global_best = min(particles, key=lambda p: obj_func(p.pos)).pos.copy()

    t = 0
    while t < max_iter:
        for particle in particles:
            particle.move(global_best)
            particle.update_best(obj_func)
        
        best_particle = min(particles, key=lambda p: obj_func(p.best))
        if obj_func(best_particle.best) < obj_func(global_best):
            global_best = best_particle.best.copy()

        t += 1

    return global_best, obj_func(global_best)

# Run the program

best_pos, best_val = pso(himmelblau)
print("Final best position:", best_pos)
print("Final best value:", best_val)
