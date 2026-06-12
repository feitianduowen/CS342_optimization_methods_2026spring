<br><br>

<br>

# Homework14_12412639_ WangSiyu

The lab problem is to maximize $f_1=x_1,\ f_2=x_2$ subject to $x_1+x_2\le 1,\ x_1,x_2\ge0$, so the Pareto front is the line segment from $(0,1)$ to $(1,0)$. I use the lecture definition that hypervolume is the dominated region bounded by the reference point, and IGD is the average distance from each reference point on the Pareto front to its nearest solution.

Let every Pareto solution be written as
$
p(t)=(t,1-t),\quad 0\le t\le 1.
$

### Final answers

| ### Task | Optimal solution set                                  |
| -------- | ----------------------------------------------------- |
| 1        | ${(0.5,0.5)}$                                         |
| 2        | ${(1,0)}$                                             |
| 3        | ${(1/3,2/3),(2/3,1/3)}$                               |
| 4        | ${(0,1),(1,0)}$                                       |
| 5        | ${(0,1),(1/4,3/4),(1/2,1/2),(3/4,1/4),(1,0)}$         |
| 6        | ${(0.1,0.9),(0.3,0.7),(0.5,0.5),(0.7,0.3),(0.9,0.1)}$ |

### Working

### Task 1.

<img src="pic\w14t1.png" style="zoom:50%;" /> 

Reference point $(0,0)$, one solution $p(t)$:
$HV=t(1-t).$
This is maximized at $t=1/2$.
So the solution is $(1/2,1/2)$​.

------



### Task 2. 

<img src="pic\w14t2.png" style="zoom:50%;" />

Reference point $(0,-1)$, one solution $p(t)$:
$HV=t[(1-t)-(-1)]=t(2-t).$
This is maximized at (t=1).
So the solution is $(1,0)$.

---



### Task 3. 

<img src="pic\w14t3.png" style="zoom:50%;" />

Reference point $(0,0)$, two solutions (p(t_1),p(t_2)$, where (0\le t_1<t_2\le1):
$
$HV=t_1(1-t_1)+(t_2-t_1)(1-t_2)$.
The optimum is
$t_1=1/3,\quad t_2=2/3.$
So the two solutions are $(1/3,2/3)$ and $(2/3,1/3)$.

---



### Task 4. 

<img src="pic\w14t4.png" style="zoom:50%;" />

Reference point $(-2,-2)$, two solutions. The hypervolume is maximized by including both extreme points of the Pareto front:
$
(0,1),\quad (1,0).
$

---



### Task 5.

<img src="pic\w14t5.png" style="zoom:50%;" />

Reference point $(-2,-2)$, five solutions. Because the reference point is far below and to the left, the two boundary points should be included. The remaining three points are equally spaced on the line segment.
So the optimal five solutions are
$
(0,1),\ (1/4,3/4),\ (1/2,1/2),\ (3/4,1/4),\ (1,0).
$

---



### Task 6. 

<img src="pic\w14t6.png" style="zoom:50%;" />For IGD with infinitely many uniformly distributed reference points on the Pareto front, the best five solutions are the midpoints of five equal intervals on the front. Therefore
$
t=\frac{1}{10},\frac{3}{10},\frac{5}{10},\frac{7}{10},\frac{9}{10}.
$
So the IGD-minimizing set is
$$
(0.1,0.9),\ (0.3,0.7),\ (0.5,0.5),\ (0.7,0.3),\ (0.9,0.1).
$$