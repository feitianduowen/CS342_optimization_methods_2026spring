import pandas as pd
import numpy as np
import time
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, PULP_CBC_CMD
import math
import random

# Load data
try:
    values = pd.read_excel('value for 100 items.xlsx', header=None).values.flatten()
    weights = pd.read_excel('weight for ten constraints of 100 item problem.xlsx', header=None).values
    capacities = pd.read_excel('capacity for ten constraints of 100 item problem.xlsx', header=None).values.flatten()
    
    num_items = len(values)
    num_constraints = len(capacities)
except Exception as e:
    print(e)
    exit()

print("Data loaded")

# (i) Heuristic method (greedy)
start_time = time.time()
ratios = values / np.sum(weights, axis=1) # Value over total weight
sorted_indices = np.argsort(ratios)[::-1]

heuristic_solution = np.zeros(num_items)
current_weights = np.zeros(num_constraints)
heuristic_obj = 0

for idx in sorted_indices:
    if np.all(current_weights + weights[idx, :] <= capacities):
        heuristic_solution[idx] = 1
        current_weights += weights[idx, :]
        heuristic_obj += values[idx]

heuristic_time = time.time() - start_time
print(f"(i) Heuristic: obj = {heuristic_obj}, time = {heuristic_time:.4f}s")


# (ii) Simulated Annealing
def get_initial_temp():
    return 100.0

def evaluate(sol):
    return np.sum(sol * values)

def is_feasible(sol):
    return np.all(np.sum(sol[:, np.newaxis] * weights, axis=0) <= capacities)

start_time = time.time()
sol = heuristic_solution.copy()
best_sol = sol.copy()
best_obj = heuristic_obj

temp = get_initial_temp()
alpha = 0.99
max_iter = 1000

for i in range(max_iter):
    # Neighborhood: flip a random item
    idx = random.randint(0, num_items - 1)
    new_sol = sol.copy()
    new_sol[idx] = 1 - new_sol[idx]
    
    if is_feasible(new_sol):
        new_obj = evaluate(new_sol)
        delta = new_obj - evaluate(sol)
        
        if delta > 0 or random.random() < math.exp(delta / temp):
            sol = new_sol
            if new_obj > best_obj:
                best_sol = new_sol
                best_obj = new_obj
    
    temp *= alpha

sa_time = time.time() - start_time
print(f"(ii) SA: obj = {best_obj}, time = {sa_time:.4f}s")


# (iii) LP relaxation + heuristic round
start_time = time.time()
prob_lp = LpProblem("Knapsack_LP", LpMaximize)
x_lp = [LpVariable(f"x_{j}", 0, 1, cat="Continuous") for j in range(num_items)]

prob_lp += lpSum(values[j] * x_lp[j] for j in range(num_items))
for i in range(num_constraints):
    prob_lp += lpSum(weights[j, i] * x_lp[j] for j in range(num_items)) <= capacities[i]

prob_lp.solve(PULP_CBC_CMD(msg=False))
lp_vals = np.array([v.varValue for v in x_lp])
# Rounding
sorted_lp_indices = np.argsort(lp_vals)[::-1]
lp_heuristic_solution = np.zeros(num_items)
current_weights = np.zeros(num_constraints)
lp_heuristic_obj = 0

for idx in sorted_lp_indices:
    if lp_vals[idx] > 0.001 and np.all(current_weights + weights[idx, :] <= capacities):
        lp_heuristic_solution[idx] = 1
        current_weights += weights[idx, :]
        lp_heuristic_obj += values[idx]

lp_time = time.time() - start_time
print(f"(iii) LP + Creation: obj = {lp_heuristic_obj}, time = {lp_time:.4f}s (LP obj = {prob_lp.objective.value()})")


# (iv) ILP solver
start_time = time.time()
prob_ilp = LpProblem("Knapsack_ILP", LpMaximize)
x_ilp = [LpVariable(f"x_{j}", 0, 1, cat="Integer") for j in range(num_items)]

prob_ilp += lpSum(values[j] * x_ilp[j] for j in range(num_items))
for i in range(num_constraints):
    prob_ilp += lpSum(weights[j, i] * x_ilp[j] for j in range(num_items)) <= capacities[i]

prob_ilp.solve(PULP_CBC_CMD(msg=False))
ilp_time = time.time() - start_time
print(f"(iv) ILP: obj = {prob_ilp.objective.value()}, time = {ilp_time:.4f}s")
