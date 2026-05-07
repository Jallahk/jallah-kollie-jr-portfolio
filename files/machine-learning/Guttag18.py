import random
import numpy as np

# # Figure 18-1 on page 396
def roll_die():
    return random.choice([1,2,3,4,5,6])

# #Used later in chapter
# def roll_die():
#     return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])

def check_pascal(num_trials):
    """Assumes num_trials is an int > 0
       Prints an estimate of the probability of winning"""
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print('Probability of winning =', num_wins/num_trials)
    
# check_pascal(1000000)

# # Figure 18-6 from page 407
def throw_needles(num_needles):
    in_circle = 0
    for Needles in range(1, num_needles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            in_circle += 1
    #Counting needles in one quadrant only, so multiply by 4
            
    return 4*(in_circle/num_needles)

def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needles(num_needles)
        estimates.append(pi_guess)
    std_dev = np.std(estimates)
    cur_est = sum(estimates)/len(estimates)
    print('Est. =', str(round(cur_est, 5)) + ',',
          'Std. dev. =', str(round(std_dev, 5)) + ',',
          'Needles =', num_needles)
    return (cur_est, std_dev)

def est_pi(precision, num_trials):
    num_needles = 1000
    std_dev = precision
    while std_dev > precision/1.96:
        cur_est, std_dev = get_est(num_needles, num_trials)
        num_needles *= 2
    return cur_est

# # Code from page 407
random.seed(0)
est_pi(0.01, 100)