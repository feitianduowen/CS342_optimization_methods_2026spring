# week6

12412639 王思宇

## T1

For these calculations, we assume the solutions are ranked from $i = 1$ (the worst solution) to $i = N$ (the best solution). In a tournament with duplication (sampling with replacement), a solution of rank $i$ wins if it is the best solution drawn in the tournament. This means all $K$ drawn solutions must have a rank of $i$ or worse, and at least one must have exactly rank $i$.

1. Selection probability of the best solution ($N=10, K=2$)  The best solution ($i=10$) simply needs to be selected at least once during the $K=2$ draws.

   - The probability of *not* selecting the best solution in a single draw is $9/10$.

   - The probability of *not* selecting it in both draws is $(9/10)^2$.

     $$P(\text{best}) = 1 - \left(\frac{9}{10}\right)^2 = 1 - 0.81 = 0.19$$

     **Answer:** The selection probability is **19%**.

2. Selection probability of the i-th solution ($N=10, K=2$)  For the $i$-th solution to win, all selected solutions must have a rank $\ge i$, and at least one must be exactly $i$.

   - The probability that all $K$ solutions have rank $\ge i$ is $\left(\frac{i + 1}{10}\right)^2$.

   - The probability that all $K$ solutions have rank $> i$ is $\left(\frac{i}{10}\right)^2$.

   - The probability of the $i$-th solution winning is the difference between these two:

     $$P(i) = \left(\frac{i+1}{10}\right)^2 - \left(\frac{i}{10}\right)^2 = \frac{2i+1}{100}$$

3. Selection probability of the i-th solution ($N=10, K=3$)  Using the exact same logic as above, but with a tournament size of $K=3$:

   $$P(i) = \left(\frac{i+1}{10}\right)^3 - \left(\frac{i}{10}\right)^3$$

------

## T2

**(1) Advantages and Disadvantages of Temperature Strategies** 

- **(i) Gradually Decreasing Temperature:**
  - **Advantages:** This perfectly balances "exploration" and "exploitation." High initial temperatures allow the algorithm to escape local optima by accepting worse solutions. As it cools, it naturally transitions to fine-tuning and exploiting the best found regions, mathematically guaranteeing convergence to a global optimum if cooled slowly enough.
  - **Disadvantages:** It is computationally expensive and requires careful tuning of the cooling schedule (initial temperature, final temperature, and the cooling rate).
- **(ii) Fixed Temperature:**
  - **Advantages:** It is highly simplified and easy to implement, with only one parameter to track.
  - **Disadvantages:** It cannot balance exploration and exploitation. If the fixed temperature is too high, the algorithm acts like a random walk and never converges. If it is too low, it acts like a greedy search and easily gets permanently trapped in local optima.



**(2) Which task is easier to appropriately specify?** 

- **Answer:** Task (i)—specifying the initial, final, and cooling schedule—is practically **easier** to appropriately specify for a successful optimization process.

- **Reasoning:** While strategy (ii) has fewer parameters, it is usually impossible to find a *single* fixed temperature that allows an algorithm to simultaneously explore the search space and converge accurately. Strategy (i) naturally mimics physical annealing; using standard heuristic defaults (like a very high initial temperature and a simple geometric decay rate like 0.99) will almost always yield reasonably good results without needing mathematically perfect precision.

  

## T3

The **$(\mu, \lambda)$ ES (The standard comma strategy)** is generally considered the best and most robust mechanism for complex continuous optimization.

**Reasoning:** 

- **Self-Adaptation:** In Evolution Strategies (ES), parameters like mutation step sizes are self-adapted. Elitist "plus" strategies like $(\mu+\lambda)$ or $(\mu+\mu)$  preserve parents if they are better than their offspring. This can result in parents with bad step sizes (e.g., zero step size) being stuck in the population forever if they accidentally achieved a good fitness value.

  

- **Escaping Local Optima:** By forgetting the parents entirely each generation (the comma strategy), the $(\mu, \lambda)$ strategy forces the algorithm to explore new points, making it much better at escaping local optima and adapting to dynamic or noisy landscapes.

  

- **Diversity and Exploration:** With a sufficiently large offspring pool (e.g., $\lambda=500$), it maintains high exploration diversity before selecting the best $\mu$ individuals. This is vastly superior to random search $(1,1)$ , simple fast moves $(1+1)$ , steady-state algorithms $(\mu+1)$ , or simpler models like $(\mu,\mu)$.