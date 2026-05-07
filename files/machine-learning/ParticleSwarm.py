from particleClass import *

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

from random import random  

def makeSwarm(size, dim, bound):
    swarm = []
    for _ in range(size):
        p = Particle(dim)
        p.initialPos(bound, firstQuad=True)  # positions between 0 and 5
        p.best = np.copy(p.pos)  # initialize best to starting position
        swarm.append(p)
    return swarm

def update_velocity(p, g_best, alpha=2, beta=2):
    new_velocity = np.zeros(p.dim)
    for i in range(p.dim):
        r1 = random()
        r2 = random()
        pbest = alpha * r1 * abs(p.best[i] - p.pos[i])
        gbest = beta * r2 * abs(g_best[i] - p.pos[i])
        new_velocity[i] = p.vel[i] + pbest + gbest
    return new_velocity

def update_position(p):
    return p.pos + p.vel

def pso(dim, size, max_iter, bound):
    # 1️Make the swarm
    swarm = makeSwarm(size, dim, bound)
    
    # 2️Initialize global best
    g_best = np.copy(swarm[0].best)
    g_best_val = himmelblau(g_best)

    #  Check if any other particle is better at the start
    for p in swarm:
        val = himmelblau(p.best)
        if val < g_best_val:
            g_best = np.copy(p.best)
            g_best_val = val

    # 3 Main loop
    #for it in range(max_iter):
       # print(f"\nIteration {it + 1}")
        
        idx = 0  
        for p in swarm:
            # Update velocity & position
            p.vel = update_velocity(p, g_best)
            p.pos = update_position(p)
            
            # Keep positions inside [0, bound] 
            for i in range(p.dim):
                if p.pos[i] < 0:
                    p.pos[i] = 0
                elif p.pos[i] > bound:
                    p.pos[i] = bound

            # Update personal best using the class method
            p.updateBest(himmelblau)

            # Update global best if needed
            val = himmelblau(p.best)
            if val < g_best_val:
                g_best = np.copy(p.best)
                g_best_val = val
            
            #print(f"Particle {idx}: pos={p.pos}, val={himmelblau(p.pos)}")
            #idx += 1

        #print(f"Global best so far: pos={g_best}, val={g_best_val}")

    return g_best, g_best_val


# Run with 500 iterations 
best_pos, best_val = pso(dim=2, size=30, max_iter=500, bound=5)
print("\nFinal best position:", best_pos)
print("Final best value:", best_val)
