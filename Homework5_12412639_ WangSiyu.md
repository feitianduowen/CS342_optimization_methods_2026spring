<br><br>

<br>

# Homework5_12412639_ WangSiyu

<div style="page-break-after: always;"></div>

#### **Q1 - Pruning Calculation in 8-City TSP**

**Title: Pruning in 8-City Traveling Salesperson Problem (TSP)**

- **Problem Context**:

  - Search tree contains 42 nodes at depth level 2.

    

  - Initial Upper Bound (Greedy Solution): Tour length = 10.

<div style="page-break-after: always;"></div>

- **Pruning Logic**:

  - 

    **Condition**: Terminate a node if its **Lower Bound (LB) > 10**.

    

    

  - 

    **LB Calculation**: $LB = \text{Current Path Length} + \text{Distance to Farthest City} + \text{Distance from Farthest to Start}$.

    
<div style="page-break-after: always;"></div>


- **Implementation**:

  - At Depth 2, two cities are visited from Start (City 0).

  - Examine all 42 combinations (e.g., 0→1→2).

  - Paths straying too far (e.g., towards City 3 or 7) often exceed the threshold of 10.

    
<div style="page-break-after: always;"></div>


  - 

    **Goal**: Identify and prune suboptimal paths early to significantly reduce tree size.

    

    

<div style="page-break-after: always;"></div>

#### **Q2 - Lower Bound Estimation in Flow Shop Scheduling**

**Title: Lower Bound Specification for m-Machine n-Job Flow Shop**

- 

  **Objective**: Minimize the maximum completion time (**Makespan**).

  

  

- 

  **State**: Each node represents a partial schedule where $k$ jobs are sequenced.

  
<div style="page-break-after: always;"></div>


- **Lower Bound Estimation Strategy**:

  1. **Scheduled Time**: Exact completion time for the $k$ sequenced jobs on each machine.

  2. 

     **Unscheduled Processing**: Sum of minimum processing times for the remaining $n-k$ jobs on a bottleneck machine.

     
<div style="page-break-after: always;"></div>


  3. **Tail Time**: Minimum theoretical time to complete remaining processes on subsequent machines after the bottleneck.

- **Decision**: If $LB > \text{Current Best Makespan}$, terminate the search at this node.

<div style="page-break-after: always;"></div>

#### **Slide 3: Q3 - Practical Limits of Branch and Bound (B&B)**

**Title: Computational Scalability of B&B for 10-Machine Problems**

- **Theoretical Complexity**:

  - An $n$-job problem has $n!$ possible solutions.

    

    

  - 

    **$n=14$**: ~87 billion solutions (Manageable with good algorithms).

    

    

  - 

    **$n=100$**: Unrealistically large search space.

    
<div style="page-break-after: always;"></div>


- **B&B Efficiency**:

  - Reduces computation by pruning nodes that cannot yield optimal results.

    

    

  - However, it cannot fully overcome the exponential growth of NP-hard problems.
<div style="page-break-after: always;"></div>
- **Estimated Limits**:

  - For $m=10$, absolute optimal solutions are typically achievable for $n \approx 20 \text{--} 30$ within a day.

  - For larger $n$ (e.g., 100), metaheuristics (Genetic Algorithms, SA, TS) must be used to find near-optimal solutions.

    

    