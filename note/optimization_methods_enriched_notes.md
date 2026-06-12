# Optimization Methods（优化方法）课程知识点整理强化版

> 本文档在原有章节整理的基础上，结合课件与课后实验内容进行扩展。  
> 复习时建议按“概念—模型—算法流程—实验题—易错点”的顺序理解，而不是只背结论。  
> 文中公式统一使用 Markdown 数学格式：行内公式如 $n$，行外公式使用：
>
> $$
> \text{formula}
> $$

---

# 第1章 Introduction

## 1.1 本章定位

第1章是整门课的总入口，重点不是某一个具体算法，而是建立优化问题的基本语言。后面所有内容，无论是贪心算法、局部搜索、线性规划、非线性优化，还是多目标优化，本质上都可以放回这个框架中理解：

- 要优化什么；
- 可以选择什么；
- 有哪些限制；
- 什么样的解算好；
- 算法如何在有限时间内找到足够好的解。

因此第1章最重要的是掌握优化问题的基本构成，以及优化与机器学习、组合优化、连续优化之间的关系。

## 1.2 优化问题的基本形式

一个优化问题通常包含三部分：决策变量、目标函数、约束条件。最一般的最小化问题可以写成：

$$
\min_{x\in X} f(x)
$$

其中：

- $x$ 是决策变量；
- $X$ 是可行域，也就是所有满足约束条件的解的集合；
- $f(x)$ 是目标函数；
- 优化目标是在 $X$ 中找到使 $f(x)$ 最小的 $x$。

如果是最大化问题，也可以写成：

$$
\max_{x\in X} f(x)
$$

很多最大化问题可以转化为最小化问题：

$$
\max f(x)\quad \Longleftrightarrow \quad \min -f(x)
$$

因此在理论分析中，经常只讨论最小化形式。

## 1.3 决策变量、目标函数与约束条件

### 1. 决策变量

决策变量回答“我们要决定什么”。例如：

- TSP 中，决策变量是一条访问所有城市的路径；
- 背包问题中，决策变量是每个物品是否放入背包；
- 线性规划中，决策变量可能是每种产品生产多少；
- 神经网络训练中，决策变量是权重向量 $w$。

### 2. 目标函数

目标函数回答“什么样的解更好”。例如：

- TSP：总路径长度越短越好；
- 背包问题：总价值越大越好；
- 机器学习：训练误差或损失函数越小越好；
- 多目标优化：多个目标同时考虑，例如成本低、质量高、时间短。

### 3. 约束条件

约束条件回答“哪些解是允许的”。例如：

- 背包容量不能超过上限；
- 变量必须非负；
- 某些变量必须是整数；
- 多目标问题中的决策变量必须满足问题定义的可行条件。

如果没有约束，就称为无约束优化；如果存在等式或不等式限制，就称为约束优化。

## 1.4 可行解、最优解、目标值

一个满足所有约束条件的解称为可行解。所有可行解组成可行域 $X$。

若 $x^*$ 是最小化问题的全局最优解，则它满足：

$$
f(x^*) \le f(x),\quad \forall x\in X
$$

其中 $f(x^*)$ 称为最优目标值。

需要注意：最优解不一定唯一。可能存在多个不同的解 $x_1^*,x_2^*,\ldots$，它们具有相同的最优目标值。

## 1.5 Learning and Optimization 的关系

课件用神经网络学习作为例子。假设训练数据为：

$$
(x_1,y_1),(x_2,y_2),\ldots,(x_m,y_m)
$$

神经网络输出为 $f(x)$，权重向量为 $w$。常见的训练误差可以写成：

$$
z(w)=\frac{1}{m}\sum_{i=1}^{m}(y_i-f(x_i))^2
$$

学习过程可以看成调节权重 $w$，使训练误差 $z(w)$ 尽可能小：

$$
\min_w z(w)
$$

因此，从形式上看，learning 可以被视为 optimization。

但是，二者的最终目标并不完全相同。优化更关注给定目标函数在给定数据或给定可行域上的最优值；学习更关注未见过数据上的表现，也就是 generalization。

## 1.6 训练误差与测试误差

训练误差是模型在训练数据上的误差：

$$
z_{\text{train}}(w)=\frac{1}{m}\sum_{i=1}^{m}(y_i-f(x_i))^2
$$

测试误差是模型在测试数据上的误差。若测试数据为：

$$
(x_{m+1},y_{m+1}),\ldots,(x_{m+n},y_{m+n})
$$

则测试误差可以写成：

$$
z_{\text{test}}(w)=\frac{1}{n}\sum_{i=m+1}^{m+n}(y_i-f(x_i))^2
$$

学习的最终目标通常不是让训练误差最低，而是希望测试误差低。训练误差过低但测试误差很高，说明模型可能发生过拟合。

## 1.7 优化问题的分类

### 1. 按变量类型分类

连续优化：

$$
x\in \mathbb{R}^n
$$

离散优化或组合优化：

$$
x\in \{0,1\}^n
$$

或 $x$ 是一个排列、子集、路径、图结构等。

### 2. 按目标数量分类

单目标优化：

$$
\min f(x)
$$

多目标优化：

$$
\min \big(f_1(x),f_2(x),\ldots,f_m(x)\big)
$$

当目标数量很多时，通常称为 many-objective optimization。

### 3. 按约束类型分类

无约束优化：

$$
\min f(x),\quad x\in \mathbb{R}^n
$$

约束优化：

$$
\min f(x)
$$

$$
\text{subject to } g_i(x)\le 0,\quad h_j(x)=0
$$

### 4. 按函数性质分类

线性规划：

$$
\max c^Tx
$$

$$
\text{subject to } Ax\le b,\quad x\ge 0
$$

非线性规划：目标函数或约束中至少有一个是非线性的。

## 1.8 Local solution 与 Global solution

局部最优解是指在某个邻域内没有更好的解。对于最小化问题，若存在一个邻域 $N(x)$，使得：

$$
f(x)\le f(y),\quad \forall y\in N(x)
$$

则 $x$ 是局部最优解。

全局最优解要求在整个可行域内最好：

$$
f(x^*)\le f(x),\quad \forall x\in X
$$

二者的区别是：局部最优只与邻域有关，全局最优与整个可行域有关。局部搜索算法通常容易找到局部最优，但不保证找到全局最优。

## 1.9 Approximate solution 与 Near-optimal solution

Approximate solution 是由近似算法得到的解。它可能很好，也可能很差，甚至可能刚好是最优解，但算法本身通常不知道它是否最优。

Near-optimal solution 通常表示目标函数值接近最优值的解。例如，若最优值为 $f(x^*)$，某个解 $x$ 满足：

$$
f(x)-f(x^*)\le \epsilon
$$

则可以说它在目标值意义上接近最优解。但课件强调，“near”并没有统一严格的数学定义，具体取决于问题背景。

## 1.10 Multi-modal optimization

若一个优化问题存在多个全局最优解，则可以称为 multi-modal optimization。此时算法目标可能不是只找一个最优解，而是尽可能找到多个全局最优解，甚至有时也希望找到多个高质量局部最优解。

这类问题在工程设计、机器学习模型选择、多峰函数优化中很常见。

## 1.11 第1章实验重点

第1周实验主要训练“问题规模”的理解。

### 1. TSP 的不同 tour 数量

对称 TSP 中，若有 $n$ 个城市，所有排列数量是 $n!$。但是：

- 从不同城市开始的循环路径是同一条 tour；
- 正向和反向路径的长度相同，也视为同一条 tour。

因此不同 tour 数量为：

$$
\frac{(n-1)!}{2}
$$

### 2. Load balancing 问题

在机器相同的情况下，机器编号互换不产生新的解。例如把所有 job 放入机器1，与把所有 job 放入机器2，在本质上是同一种分组方式。

因此 load balancing 的解空间不是简单的 $m^n$，而需要考虑机器相同导致的等价性。这个问题本质上接近“把 $n$ 个 job 分成若干组”的 grouping problem。

## 1.12 第1章复习要点

本章需要会回答：

- 什么是优化问题；
- 什么是决策变量、目标函数、约束条件；
- 什么是可行解、局部最优解、全局最优解；
- 为什么 learning 可以被看成 optimization；
- learning 与 optimization 的最终目标有什么不同；
- TSP 的 tour 数为什么不是 $n!$；
- 相同机器的 load balancing 为什么不能简单按机器编号计数。

---

# 第2章 Greedy Algorithms for Combinatorial Optimization

## 2.1 本章定位

第2章开始进入组合优化。组合优化的特点是可行解数量巨大，很难直接枚举所有解。Greedy algorithm 是最容易理解的一类启发式算法：每一步都做当前看起来最好的选择。

贪心算法通常很快，也常用于生成初始解。但它的缺点也很明显：局部选择不一定导向全局最优。

## 2.2 Greedy algorithm 的基本思想

贪心算法的基本框架是：

1. 从空解或某个初始状态开始；
2. 在每一步选择当前看来最好的局部操作；
3. 将该操作加入当前解；
4. 重复直到得到完整解。

它的核心特点是“不回头”。一旦做出某一步选择，后面通常不会撤销。

## 2.3 贪心算法的优点

贪心算法的优点包括：

- 实现简单；
- 计算速度快；
- 不需要复杂参数；
- 对某些问题可以得到最优解；
- 对很多复杂问题可以得到一个可接受的初始解。

例如在后续局部搜索中，greedy solution 经常被用作初始解。

## 2.4 贪心算法的局限

贪心算法的主要问题是只关注当前局部最优，不考虑长期影响。它可能在前几步选择了看似很好的元素，但导致后面必须付出很大代价。

因此，贪心算法通常不能保证全局最优。

## 2.5 TSP 中的 Nearest Neighbor Greedy Method

TSP 的目标是找到一条最短 tour，使其从某个城市出发，访问每个城市一次，并回到起点。

输入为：

- 城市集合；
- 城市之间距离 $d_{ij}$；
- 通常假设 $d_{ij}=d_{ji}$。

目标为：

$$
\min \sum_{(i,j)\in T} d_{ij}
$$

Nearest Neighbor Greedy Method 的流程是：

1. 任意选择一个起始城市；
2. 从当前城市出发，选择尚未访问城市中距离最近的城市；
3. 移动到该城市；
4. 重复直到所有城市都被访问；
5. 返回起始城市。

该算法的直观想法是“每一步走最近的城市”。但它可能造成最后回到起点时出现很长边，从而使总路径变差。

## 2.6 TSP 中 greedy solution 为什么可能很差

在 TSP 中，局部最近不代表整体最短。一个典型现象是：前面一直选择很近的城市，最后可能被迫连接两个距离很远的城市。

另一个重要几何判断是：在欧氏 TSP 中，如果 tour 中存在两条相交边，那么该 tour 通常不是最优的。因为可以通过交换边消除交叉，使路径更短。

若边 $(a,b)$ 与 $(c,d)$ 相交，通常可以用 $(a,c)$ 与 $(b,d)$ 代替，从而缩短路径。这个思想也是第3章 inversion 或 two-edge change 的基础。

## 2.7 背包问题中的贪心失败

0-1 背包问题形式为：

$$
\max \sum_{i=1}^{n} v_i x_i
$$

$$
\text{subject to } \sum_{i=1}^{n} w_i x_i\le W
$$

$$
x_i\in \{0,1\}
$$

常见贪心策略包括：

- 按价值 $v_i$ 从大到小选择；
- 按重量 $w_i$ 从小到大选择；
- 按性价比 $\frac{v_i}{w_i}$ 从大到小选择。

但在 0-1 背包中，这些策略都不一定最优。因为某个看似性价比高的小物品，可能会占用容量，使得后面无法选择一个价值极高的大物品。

## 2.8 Load balancing 中的贪心失败

Load balancing 问题通常可以表述为：把 $n$ 个 job 分配到 $m$ 台相同机器上，使最大完成时间最小。

若 job $i$ 的处理时间为 $p_i$，机器 $j$ 上的任务集合为 $S_j$，则机器 $j$ 的负载为：

$$
L_j=\sum_{i\in S_j}p_i
$$

makespan 为：

$$
C_{\max}=\max_{1\le j\le m}L_j
$$

目标是：

$$
\min C_{\max}
$$

一种常见 greedy 方法是每次把下一个 job 分给当前负载最小的机器。这个策略很自然，但可能得到接近最优值两倍的 makespan。

## 2.9 第2章实验重点

实验要求构造反例，说明 greedy 可能非常差。

### 1. 背包问题反例

需要构造一个例子，使 greedy solution 的总价值小于 optimal solution 的 $1/100$。这类例子的构造思路是：让 greedy 先选一个看似局部最优但整体价值很低的物品，然后阻止它选择真正高价值的物品。

### 2. TSP 反例

需要构造一个例子，使 greedy tour length 超过 optimal tour length 的两倍。构造思路是：安排城市位置，使 greedy 一开始被局部短边吸引，最后被迫走一条特别长的边。

### 3. Load balancing 反例

需要构造一个例子，使 greedy makespan 接近 optimal makespan 的两倍。构造思路是：让 greedy 在前期产生不均衡分配，最后一个大任务使某台机器负载接近两倍最优值。

## 2.10 第2章复习要点

本章需要重点掌握：

- greedy 的基本思想；
- greedy 为什么快；
- greedy 为什么可能不是最优；
- TSP 中 nearest neighbor greedy 的流程；
- 背包、TSP、load balancing 中 greedy 失败的原因；
- greedy solution 为什么常作为 local search 的初始解。

---

# 第3章 Local Search and Neighborhood Structures

## 3.1 本章定位

第3章是在第2章基础上的改进。既然 greedy solution 通常不是最优，就可以尝试对它做小修改。如果小修改能使解变好，就接受修改。这个过程就是 local search。

Local search 是组合优化中非常重要的基本思想。后面的 VNS、SA、TS、EA 都可以看作是在不同方式上扩展 local search。

## 3.2 Local Search 的基本机制

Local Search 的基本流程为：

1. 构造一个初始解 $x$；
2. 根据邻域结构 $N(x)$ 生成当前解的邻居；
3. 如果存在更好的邻居 $x'$，则移动到 $x'$；
4. 重复上述过程；
5. 若没有更好的邻居，则停止。

对于最小化问题，如果：

$$
f(x')<f(x)
$$

则 $x'$ 是一个改进解，可以接受。

## 3.3 邻域结构 Neighborhood Structure

邻域结构定义“什么样的解可以由当前解一步得到”。给定当前解 $x$，其邻域记为：

$$
N(x)=\{x'\mid x'\text{ can be generated from }x\text{ by one move}\}
$$

邻域结构是局部搜索的核心。它决定：

- 每一步可以探索多少候选解；
- 搜索速度；
- 能否跳出某些局部结构；
- 最终得到的 local optimum 是什么。

## 3.4 Local optimum 依赖于邻域结构

一个解是否是局部最优，取决于邻域定义。若在邻域 $N_1(x)$ 下没有更好解，则 $x$ 是 $N_1$ 下的局部最优。但若换成更大的邻域 $N_2(x)$，可能存在更好的解。

例如：

$$
N_1(x)\subset N_2(x)
$$

如果 $x$ 是 $N_2$ 下的局部最优，则它一定也是 $N_1$ 下的局部最优。但反过来不一定成立。

## 3.5 First Move 与 Best Move

### First Move

First Move 策略是：扫描邻居时，只要发现第一个改进解，就立刻移动。

优点：

- 计算量小；
- 每一步速度快；
- 适合邻域很大的情况。

缺点：

- 可能错过更好的邻居；
- 搜索路径受邻居扫描顺序影响较大。

### Best Move

Best Move 策略是：检查所有邻居，选择其中最好的改进解。

优点：

- 每一步改进幅度通常更大；
- 搜索过程更稳定。

缺点：

- 需要评价所有邻居；
- 计算成本高；
- 最终解质量不一定总是优于 First Move。

课件强调：First Move 通常计算负担更小，但最终解质量不能简单判断哪个一定更好。

## 3.6 TSP 中的常见邻域结构

设 TSP 有 $n$ 个城市，一个 tour 可以看成一个长度为 $n$ 的排列。

### 1. Adjacent Two-City Change

交换相邻两个城市。例如：

$$
(1,2,3,4,5)\rightarrow(1,3,2,4,5)
$$

如果把 tour 当作环，则相邻边数量为 $n$，因此邻居数量通常为：

$$
n
$$

如果把排列线性表示并不考虑首尾相邻，则邻居数量为：

$$
n-1
$$

考试或实验中需要根据课件定义判断是否把 tour 视为环。

### 2. Arbitrary Two-City Change

任意选择两个城市交换位置。邻居数量为：

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

它包含 adjacent two-city change。

### 3. Insertion / Shift

选择一个城市，将它从当前位置移除，并插入到另一个位置。

若选择要移动的城市有 $n$ 种，插入位置在移除该城市后有 $n-1$ 种，则邻居数量通常为：

$$
n(n-1)
$$

但若不同插入方式产生相同 tour，则需要去重，具体以实验定义为准。

### 4. Inversion / Arbitrary Two-Edge Change

选择 tour 中的一段，将该段顺序反转。例如：

$$
(1,2,3,4,5,6)\rightarrow(1,2,5,4,3,6)
$$

Inversion 在 TSP 中非常重要，因为它可以消除交叉边。常见邻居数量为：

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

如果排除长度为 $0$ 或 $1$ 的无效反转，或考虑 tour 的环状等价，公式可能略有调整。

### 5. Arbitrary Three-City Change

任意选三个城市并重新排列。选择三个城市有：

$$
\binom{n}{3}
$$

三个城市的排列数为 $3!=6$，其中原排列不算新邻居，因此每组三个城市有 $5$ 种新排列。所以邻居数量常写为：

$$
5\binom{n}{3}
$$

若课件把 two-city change 也包含在 arbitrary three-city change 中，需要根据定义进一步说明。

## 3.7 邻域大小与搜索效率

邻域越小，单步搜索越快，但容易陷入较差局部最优。邻域越大，搜索能力更强，但每一步计算成本更高。

设每评价一个邻居需要时间 $O(1)$，如果邻居数量为 $|N(x)|$，Best Move 每步计算量大约为：

$$
O(|N(x)|)
$$

因此，邻域结构设计本质上是在搜索质量与计算成本之间做平衡。

## 3.8 Greedy + Local Search

实际组合优化中常见策略是：

1. 用 greedy 快速得到一个初始解；
2. 用 local search 改进 greedy solution；
3. 若陷入局部最优，再用 restart、VNS、SA、TS 等方法继续改进。

这是后续章节的主线。

## 3.9 第3章实验重点

实验要求计算不同 TSP 邻域结构的邻居数量。答题时要说明：

- 一次 move 需要选择几个位置；
- 是否考虑顺序；
- 是否有无效操作；
- 是否有重复 tour；
- 是否把 tour 看作环；
- 是否把正反方向视为同一 tour。

## 3.10 第3章复习要点

本章必须掌握：

- local search 的基本流程；
- neighborhood structure 的含义；
- local optimum 依赖邻域；
- first move 与 best move 的区别；
- TSP 中 swap、insertion、inversion 的含义；
- 为什么 inversion 可以改进带交叉边的 TSP tour。

---

# 第4章 VNS, VND, Simulated Annealing, Tabu Search and Evolutionary Computation

## 4.1 本章定位

第4章继续解决 local search 的核心缺点：容易陷入局部最优。普通 local search 只接受更好解，一旦当前邻域内没有更好解就停止。

本章介绍多种改进思想：

- 用多个邻域：VNS、VND；
- 允许接受较差解：SA、TS；
- 同时维护多个解：EA、EC。

它们共同目标是平衡 wide global search 与 focused efficient search。

## 4.2 Iterated Local Search

Iterated Local Search 的思想是多次运行 local search。每次从不同初始解出发，可能收敛到不同局部最优解。

基本流程：

1. 生成初始解；
2. 执行 local search，得到局部最优解；
3. 扰动当前解或重新生成初始解；
4. 再次执行 local search；
5. 保留找到的最好解。

这种方法简单有效，但性能依赖于初始解生成方式和扰动策略。

## 4.3 Variable Neighborhood Search

VNS 的核心是使用多个邻域结构：

$$
N_1,N_2,\ldots,N_{k_{\max}}
$$

通常 $N_1$ 较小，$N_{k_{\max}}$ 较大。小邻域用于快速改进，大邻域用于跳出局部最优。

基本思想是：如果当前解在小邻域下无法改进，就尝试更大的邻域。

## 4.4 Variable Neighborhood Descent

VND 是一种确定性的变邻域下降方法。它依次使用多个邻域进行局部搜索。

典型流程：

1. 令 $k=1$；
2. 在邻域 $N_k$ 中寻找改进解；
3. 如果找到改进解，则移动并令 $k=1$；
4. 如果找不到改进解，则令 $k=k+1$；
5. 当 $k>k_{\max}$ 时停止。

VND 与普通 local search 的区别在于：普通 local search 只使用一个邻域，而 VND 使用多个邻域。

## 4.5 Knapsack 中的 VND 邻域设计

对于 0-1 背包问题，解是一个二进制向量：

$$
x=(x_1,x_2,\ldots,x_n),\quad x_i\in\{0,1\}
$$

可以设计如下邻域：

### $N_1$：单点翻转

改变一个物品的选择状态：

$$
x_i=0\rightarrow 1
$$

或：

$$
x_i=1\rightarrow 0
$$

### $N_2$：一删一加

删除一个已选物品，同时加入一个未选物品。

### $N_3$：二删一加或一删二加

通过更大范围的交换改变子集结构。

### $N_4$：随机移除若干物品后重新填充

先移除若干已选物品，再按价值、性价比或随机策略重新加入物品。

邻域越大，越可能找到更好的解，但计算量越高。

## 4.6 Simulated Annealing

Simulated Annealing 的核心是允许接受较差解，从而跳出局部最优。

对于最小化问题，若新解 $x'$ 比当前解 $x$ 更好，即：

$$
f(x')<f(x)
$$

则直接接受。若新解更差，即：

$$
f(x')\ge f(x)
$$

则以一定概率接受。常见接受概率为：

$$
P=\exp\left(-\frac{f(x')-f(x)}{T}\right)
$$

其中 $T$ 是温度。

## 4.7 温度的作用

当 $T$ 较大时，即使 $f(x')-f(x)$ 较大，接受概率也可能不低，算法更容易进行全局探索。

当 $T$ 较小时，接受较差解的概率很小，算法更接近普通 local search。

因此：

- 高温：探索性强；
- 低温：开发性强；
- 降温过程：从全局探索逐渐转向局部精细搜索。

## 4.8 Cooling Schedule

常见冷却策略包括：

### 1. 恒定高温

优点是搜索范围广，不容易陷入局部最优。缺点是难以收敛，后期仍然可能接受太多差解。

### 2. 恒定低温

优点是搜索稳定，容易局部改进。缺点是很难跳出局部最优。

### 3. 恒定中温

在探索和收敛之间折中，但参数选择仍然困难。

### 4. 快速降温

优点是计算时间短，较快进入局部搜索。缺点是可能过早冻结。

### 5. 慢速降温

优点是搜索充分，理论上更可能找到好解。缺点是计算时间长。

## 4.9 SA 实验中的背包问题

实验使用 100-item knapsack problem with 10 constraints。问题形式为：

$$
\max f(x)=\sum_{i=1}^{100}v_i x_i
$$

$$
\text{subject to } \sum_{i=1}^{100}w_{ij}x_i\le W_j,\quad j=1,2,\ldots,10
$$

$$
x_i\in\{0,1\}
$$

邻居由 Hamming distance 定义。两个二进制向量的 Hamming distance 是它们不同位置的数量。

若 $D=1$，表示翻转一个 bit；若 $D=2$，表示翻转两个 bit；若 $D=3$，表示翻转三个 bit。

## 4.10 Constraint Handling

### 1. Repair 方法

若产生不可行解，则删除某些物品，直到满足所有约束。优点是最终评价的都是可行解；缺点是 repair 策略可能影响搜索方向。

### 2. Penalty 方法

若产生不可行解，则在适应度中加入惩罚项。对于最大化问题，可写成：

$$
F(x)=f(x)-\lambda \cdot V(x)
$$

其中 $V(x)$ 是约束违反程度，$\lambda$ 是惩罚系数。

Penalty 方法的优点是可以保留不可行解的信息，缺点是惩罚系数难以选择。

## 4.11 Tabu Search

Tabu Search 也允许移动到较差解，但它使用记忆机制避免循环。

核心元素包括：

- tabu list；
- tabu tenure；
- aspiration criterion；
- neighborhood search；
- best admissible move。

Tabu list 可以记录最近访问过的解，或者记录最近使用过的 move。例如在 TSP 中，可以禁止短期内重新加入刚刚删除的边。

## 4.12 TS 与 SA 的区别

SA 的核心控制量是温度 $T$，接受差解依赖概率。

TS 的核心机制是禁忌表，通过记忆避免搜索回头。

二者都可以跳出局部最优，但方式不同：

- SA 更随机；
- TS 更有记忆；
- SA 适合早期寻找 promising region；
- TS 适合从较好初始解出发进行细致搜索。

## 4.13 Evolutionary Algorithms

Evolutionary Algorithms 是 population-based search。它不是只维护一个当前解，而是维护一组解：

$$
P=\{x_1,x_2,\ldots,x_N\}
$$

基本过程为：

1. 初始化种群；
2. 评价每个个体；
3. 选择较好个体；
4. 通过 mutation 和 crossover 产生新个体；
5. 更新种群；
6. 重复直到停止条件满足。

## 4.14 Mutation 与 Crossover

Mutation 是对一个个体进行随机扰动。例如对二进制串翻转某些 bit：

$$
0\leftrightarrow 1
$$

Crossover 是从两个父代中重组信息。例如：

$$
x^{(1)}=(1,1,0,0,1)
$$

$$
x^{(2)}=(0,0,1,1,0)
$$

通过交叉可能得到：

$$
x'=(1,1,1,1,0)
$$

Mutation 提供局部扰动和多样性，crossover 利用不同好解的结构信息。

## 4.15 Tournament Selection

Tournament selection 的流程：

1. 从种群中随机选择 $K$ 个个体；
2. 比较它们的 fitness；
3. 选择其中最好的个体作为父代。

$K$ 称为 tournament size。$K$ 越大，选择压力越强；$K=1$ 时相当于随机选择。

若种群大小为 $N$，有放回抽样，最优个体在一次 $K$-tournament 中被选中的概率为：

$$
1-\left(1-\frac{1}{N}\right)^K
$$

## 4.16 Generation Update

常见 ES 更新机制包括：

- $(1,1)$ES：类似随机搜索；
- $(1+1)$ES：父代和一个子代竞争，类似快速局部搜索；
- $(1+\lambda)$ES：一个父代生成多个子代，从父代与子代中选最好；
- $(\mu+1)$ES：稳态更新；
- $(\mu,\lambda)$ES：只从子代中选择下一代；
- $(\mu+\lambda)$ES：从父代和子代合并集合中选择下一代。

加号 $+$ 表示父代可以保留，逗号 $,$ 表示父代不直接进入下一代。

## 4.17 第4章复习要点

本章需要重点掌握：

- local search 为什么会陷入局部最优；
- VNS/VND 如何使用多个邻域；
- SA 为什么可以接受较差解；
- 温度和 cooling schedule 的影响；
- TS 的 tabu list 如何避免循环；
- EA 为什么是 population-based search；
- mutation、crossover、selection 的作用；
- tournament size 对选择压力的影响。

---

# 第5章 Branch and Bound and Subset Selection

## 5.1 本章定位

第5章主要讨论子集选择问题和分支定界思想。子集选择问题是组合优化中非常常见的一类问题，例如背包问题、特征选择、传感器选择、代表点选择、多目标优化中的 hypervolume subset selection 等。

## 5.2 子集选择问题的基本形式

给定候选集合：

$$
S_C=\{s_1,s_2,\ldots,s_n\}
$$

目标是在其中选择一个子集：

$$
S\subseteq S_C
$$

使目标函数最优：

$$
\max f(S)
$$

或：

$$
\min f(S)
$$

并满足约束，例如：

$$
g(S)\le G
$$

或：

$$
|S|=k
$$

## 5.3 搜索空间大小

若从 $n$ 个候选项中选择 $k$ 个，则可能子集数量为：

$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

当 $n$ 很大时，$\binom{n}{k}$ 会非常大，无法穷举。

例如候选集有 $500,000,000$ 个 item，即使每一步只评价一次所有候选项，贪心算法也会非常慢。

## 5.4 Knapsack Problem

0-1 背包问题是典型子集选择问题：

$$
\max \sum_{i=1}^{n}v_i x_i
$$

$$
\text{subject to } \sum_{i=1}^{n}w_i x_i\le W
$$

$$
x_i\in\{0,1\}
$$

其中：

- $v_i$ 是物品价值；
- $w_i$ 是物品重量；
- $W$ 是容量；
- $x_i=1$ 表示选择物品 $i$；
- $x_i=0$ 表示不选择物品 $i$。

## 5.5 Hypervolume Subset Selection

在多目标优化中，可能已经有一个候选解集 $S_C$，但只能保留其中 $k$ 个解。此时可以选择使 hypervolume 最大的子集：

$$
\max_{S\subseteq S_C}HV(S)
$$

$$
\text{subject to } |S|=k
$$

这个问题的难点在于：候选解数量大时，所有 $k$ 元子集数量巨大，而且 $HV(S)$ 的计算本身也可能昂贵。

## 5.6 Greedy for Subset Selection

贪心子集选择通常从空集开始：

$$
S=\emptyset
$$

每一步选择一个能带来最大边际增益的 item：

$$
s^*=\arg\max_{s\in S_C\setminus S}\big(f(S\cup\{s\})-f(S)\big)
$$

然后更新：

$$
S\leftarrow S\cup\{s^*\}
$$

重复直到满足 $|S|=k$ 或其他约束。

## 5.7 巨大候选集下如何加速 greedy

当候选集非常大时，每一步检查所有 item 不现实。可以考虑：

### 1. 随机采样候选池

每一步只从随机采样出的候选池 $C'$ 中选择最佳 item：

$$
C'\subset S_C,\quad |C'|\ll |S_C|
$$

这种方法牺牲少量质量，换取大量计算时间节省。

### 2. 分层筛选

先用低成本指标粗筛候选项，再用真实目标函数精评少量候选项。

### 3. Lazy greedy

如果目标函数具有 submodular 性质，可以用优先队列维护边际增益上界，减少重复评价。

### 4. 并行计算

将候选项分配到多个处理器或 GPU 上并行评价。

### 5. 使用代表点或聚类

先把候选项聚类，只从每个 cluster 中选代表项进入下一阶段。

## 5.8 Local Improvement for Subset Selection

在已有子集 $S$ 上，可以通过局部改进继续提升质量。

常见 move 包括：

### Add

向子集中加入一个新 item：

$$
S'\leftarrow S\cup\{s\}
$$

### Delete

删除一个已选 item：

$$
S'\leftarrow S\setminus\{s\}
$$

### Swap

删除一个已选 item，同时加入一个未选 item：

$$
S'\leftarrow S\setminus\{s_i\}\cup\{s_j\}
$$

当候选集很大时，随机选择一个待加入 item 可能低效，因此实验要求提出更聪明的选择方法，例如：

- 从高边际增益候选池中选；
- 从与当前子集互补性强的 item 中选；
- 根据历史改进记录优先选择有潜力的区域；
- 使用启发式评分筛选。

## 5.9 Branch and Bound

Branch and Bound 是精确算法思想。它通过系统地划分搜索空间，同时利用上下界剪枝，避免枚举所有解。

基本步骤：

1. Branch：把问题划分为多个子问题；
2. Bound：计算每个子问题的最好可能界；
3. Prune：如果某个子问题不可能优于当前最好解，则剪枝；
4. Search：继续扩展有希望的子问题。

对于最大化问题，如果某个子问题的上界 $UB$ 小于当前已知最好可行解值 $LB$，则可以剪枝：

$$
UB\le LB
$$

因为该子问题不可能产生更好的解。

## 5.10 第5章复习要点

需要掌握：

- 子集选择问题的数学形式；
- 背包问题如何建模；
- 为什么搜索空间是组合爆炸；
- greedy subset selection 的边际增益思想；
- 巨大候选集下如何降低计算时间；
- local improvement 中 add、delete、swap 的含义；
- branch and bound 的 branch、bound、prune 三个关键词。

---

# 第6章 Linear Programming Formulations and Applications

## 6.1 本章定位

第6章进入数学规划。与前面启发式算法不同，线性规划可以用成熟 solver 精确求解大规模连续优化问题。本章重点是建模：如何把文字问题转化为线性规划模型。

## 6.2 Linear Programming 的标准形式

线性规划要求目标函数和约束都是线性的。常见最大化形式为：

$$
\max c^Tx
$$

$$
\text{subject to } Ax\le b
$$

$$
x\ge 0
$$

等式形式为：

$$
\max c^Tx
$$

$$
\text{subject to } Ax=b
$$

$$
x\ge 0
$$

其中：

- $x$ 是决策变量向量；
- $c$ 是目标函数系数；
- $A$ 是约束矩阵；
- $b$ 是资源或需求向量。

## 6.3 建模步骤

线性规划建模通常按以下步骤：

1. 定义决策变量；
2. 写出目标函数；
3. 写出约束条件；
4. 加入非负约束或变量范围；
5. 检查所有表达式是否线性。

## 6.4 混凝土配比问题

假设有两种混凝土，第一种和第二种购买量分别为：

$$
x_1,x_2
$$

成本向量为：

$$
c=(5,1)^T
$$

目标是最小化成本：

$$
\min 5x_1+x_2
$$

如果材料需求为 cement 至少 $5$，gravel 至少 $3$，sand 至少 $4$，且两种混凝土中的成分比例形成矩阵：

$$
A=
\begin{pmatrix}
0.3 & 0.1\\
0.4 & 0.2\\
0.3 & 0.7
\end{pmatrix}
$$

需求向量为：

$$
b=
\begin{pmatrix}
5\\
3\\
4
\end{pmatrix}
$$

则模型为：

$$
\min c^Tx
$$

$$
\text{subject to } Ax\ge b
$$

$$
x\ge 0
$$

这个例子说明，建模的关键是把文字信息变成矩阵、向量和线性不等式。

## 6.5 等式约束与不等式约束

线性规划可以包含等式约束：

$$
a^Tx=b
$$

也可以包含不等式约束：

$$
a^Tx\le b
$$

或：

$$
a^Tx\ge b
$$

在实际建模中，资源上限通常写成 $\le$，最低需求通常写成 $\ge$。

## 6.6 非负约束

很多实际变量不能为负，例如生产量、购买量、运输量：

$$
x_i\ge 0
$$

如果变量还存在上界，则写为：

$$
0\le x_i\le u_i
$$

## 6.7 线性规划建模易错点

常见错误包括：

- 决策变量没有明确定义；
- 目标函数方向写反；
- 约束方向 $\le$ 与 $\ge$ 写反；
- 忘记非负约束；
- 把非线性关系误写进 LP；
- 单位不一致；
- 没有区分资源上限和最低需求。

## 6.8 第6章复习要点

必须掌握：

- LP 的基本形式；
- $c^Tx$、$Ax\le b$、$x\ge 0$ 的含义；
- 如何从文字题中抽取变量、目标、约束；
- 最小化成本与最大化利润的区别；
- 为什么 LP 要求目标和约束都是线性的。

---

# 第7章 Linear Programming Algorithms

## 7.1 本章定位

第7章关注如何求解线性规划。课件主要强调 Simplex Method 和 LP solver 的意义。复习时不一定需要手算复杂单纯形表，但必须理解 LP 最优解结构和 solver 求解思想。

## 7.2 LP 的几何解释

二维 LP 的可行域通常是由若干线性不等式围成的凸多边形。目标函数是一族平行直线。最优解通常出现在可行域的顶点上。

这也是 Simplex Method 的基础：在顶点之间移动，寻找更优顶点。

## 7.3 LP 最优解的四种情况

### 1. 唯一最优解

目标函数在某一个顶点达到最优。

### 2. 多个最优解

目标函数与可行域某条边平行，在整条边上都达到同样最优值。

### 3. 无可行解

约束之间矛盾，没有任何 $x$ 同时满足所有约束。

### 4. 无界

可行域沿目标函数改善方向无限延伸，目标值可以无限增大或无限减小。

## 7.4 Simplex Method

Simplex Method 的基本思想是：

1. 找到一个初始可行顶点；
2. 判断当前顶点是否最优；
3. 若不是，则沿某条边移动到相邻更优顶点；
4. 重复直到没有更优相邻顶点。

在标准形式中：

$$
\max c^Tx
$$

$$
\text{subject to } Ax=b,\quad x\ge 0
$$

单纯形法通过基变量和非基变量的转换实现顶点移动。

## 7.5 为什么 LP solver 很重要

LP solver 的优点包括：

- 可以求精确最优解；
- 速度快；
- 支持大规模变量；
- 使用者不必自己设计大量启发式参数；
- 可以作为 ILP 的松弛求解工具；
- 工程应用非常广泛。

## 7.6 LP relaxation

很多整数问题难以直接求解，可以先放松整数约束。例如 0-1 背包中：

$$
x_i\in\{0,1\}
$$

放松为：

$$
0\le x_i\le 1
$$

得到 LP relaxation。LP relaxation 的解可能是小数，因此不一定是原 ILP 的可行解，但它可以提供：

- 上界或下界；
- 近似解；
- 启发式构造的起点；
- branch and bound 中的 bound。

## 7.7 第7章实验重点

实验要求选择三个不同的 LP solver 或不同语言/算法求解给定问题。复习时要理解：

- solver 的输出包括最优变量值和目标值；
- 不同 solver 可能使用不同算法；
- 对同一个 LP，正确 solver 应得到一致最优值；
- 数值误差可能导致结果略有差异。

## 7.8 第7章复习要点

必须掌握：

- LP 最优解四种情况；
- Simplex Method 在顶点间移动的思想；
- LP solver 的作用；
- LP relaxation 的含义；
- 为什么 LP relaxation 可用于整数问题。

---

# 第8章 Integer Linear Programming Algorithms

## 8.1 本章定位

第8章讨论整数线性规划。ILP 与 LP 最大的区别是变量必须取整数，尤其是 0-1 变量。这使得问题从连续优化变成离散优化，求解难度显著增加。

## 8.2 ILP 的基本形式

整数线性规划可以写为：

$$
\max c^Tx
$$

$$
\text{subject to } Ax\le b
$$

$$
x_i\in \mathbb{Z}
$$

若变量只能取 $0$ 或 $1$，则为 0-1 ILP：

$$
x_i\in\{0,1\}
$$

## 8.3 LP 与 ILP 的区别

LP 的可行域是连续区域，最优解可以在凸多面体的顶点处找到。

ILP 的可行解是离散点集合，不能简单沿边移动。即使 LP relaxation 容易求解，加入整数约束后也可能变得非常困难。

## 8.4 背包问题作为 ILP

0-1 背包问题可以写成：

$$
\max \sum_{i=1}^{n}v_i x_i
$$

$$
\text{subject to } \sum_{i=1}^{n}w_i x_i\le W
$$

$$
x_i\in\{0,1\}
$$

这是典型的整数规划模型。

## 8.5 ILP Solver

ILP solver 通常结合多种技术：

- LP relaxation；
- branch and bound；
- cutting planes；
- presolve；
- heuristics；
- branch and cut。

ILP solver 的优势是可以求整数最优解；缺点是问题规模变大时计算时间可能迅速增长。

## 8.6 从 LP relaxation 构造可行整数解

若 LP relaxation 得到小数解，例如：

$$
x=(1,0.7,0,0.4)
$$

它不是 0-1 背包的可行解。需要转化为整数解。常见方法包括：

- 四舍五入；
- 按性价比排序修复；
- 删除导致违反约束的物品；
- 使用 LP 解作为启发式参考。

但这些方法不保证最优。

## 8.7 第8章实验重点

实验要求比较四类方法：

1. 用于生成 SA 初始解的启发式方法；
2. 自己设置参数的 simulated annealing；
3. 使用 LP solver 求 LP relaxation，并构造可行整数解；
4. 使用 ILP solver 直接求解。

比较指标：

- objective function value；
- total computation time。

并且需要在 100-item、200-item、400-item knapsack 上比较规模影响。

## 8.8 第8章复习要点

必须掌握：

- ILP 与 LP 的核心区别；
- 0-1 变量的含义；
- LP relaxation 的作用；
- 为什么 ILP 更难；
- heuristic、SA、LP relaxation、ILP solver 的优缺点比较。

---

# 第9章 Unconstrained Nonlinear Optimization and Gradient Descent

## 9.1 本章定位

第9章进入非线性优化。与线性规划不同，非线性优化的目标函数可能存在曲率、局部最优、鞍点、狭长谷底等问题。最基本的方法是 gradient descent。

## 9.2 无约束非线性优化模型

一般形式为：

$$
\min f(x)
$$

$$
x=(x_1,x_2,\ldots,x_n)^T\in \mathbb{R}^n
$$

其中 $f(x)$ 是非线性函数。

## 9.3 导数与下降方向

在一维情况下，如果：

$$
\frac{df}{dx}>0
$$

说明 $x$ 增大时 $f(x)$ 增大，因此要减小 $x$ 才能下降。

如果：

$$
\frac{df}{dx}<0
$$

说明 $x$ 增大时 $f(x)$ 减小，因此要增大 $x$。

因此，下降方向是负导数方向。

在多维情况下，梯度 $\nabla f(x)$ 指向函数值上升最快的方向，所以 $-\nabla f(x)$ 是最陡下降方向。

## 9.4 Gradient Descent 更新公式

梯度下降的基本更新为：

$$
x^{(k+1)}=x^{(k)}-\alpha_k\nabla f(x^{(k)})
$$

其中：

- $x^{(k)}$ 是第 $k$ 次迭代的解；
- $\alpha_k$ 是步长；
- $\nabla f(x^{(k)})$ 是当前梯度。

## 9.5 Constant Step Size

如果每一步使用相同步长 $\alpha$，则：

$$
x^{(k+1)}=x^{(k)}-\alpha\nabla f(x^{(k)})
$$

固定步长简单，但难点是选择合适的 $\alpha$。

如果 $\alpha$ 太小，收敛很慢；如果 $\alpha$ 太大，可能震荡甚至发散。

## 9.6 Steepest Descent

Steepest descent 通常使用负梯度方向，但通过 line search 确定步长：

$$
\alpha_k=\arg\min_{\alpha>0} f(x^{(k)}-\alpha\nabla f(x^{(k)}))
$$

然后更新：

$$
x^{(k+1)}=x^{(k)}-\alpha_k\nabla f(x^{(k)})
$$

它比固定步长更自适应，但每一步需要额外求解一维搜索问题。

## 9.7 Rosenbrock 函数

实验中常见 Rosenbrock 函数：

$$
f(x_1,x_2)=(1-x_1)^2+100(x_2-x_1^2)^2
$$

该函数有狭长弯曲谷底，最优解为：

$$
x^*=(1,1)
$$

梯度下降在该函数上可能非常慢，因为搜索路径容易在谷底两侧震荡。

## 9.8 第9章实验重点

实验要求：

- 选择不同初始点；
- 选择不同步长；
- 展示搜索路径；
- 比较固定步长对收敛速度和稳定性的影响；
- 在简单二次函数和 Rosenbrock 函数上观察差异。

## 9.9 第9章复习要点

必须掌握：

- 无约束非线性优化模型；
- 梯度方向和负梯度方向的意义；
- gradient descent 更新公式；
- 步长对收敛的影响；
- fixed step size 与 line search 的区别；
- Rosenbrock 函数为什么难优化。

---

# 第10章 Newton Method, Line Search and Related Modifications

## 10.1 本章定位

第10章继续讨论非线性优化，重点从一阶方法进入二阶方法。Gradient descent 只使用梯度，而 Newton method 使用二阶导数信息，因此在局部二次近似较好时收敛很快。

## 10.2 最优性条件

无约束可微最小化问题中，局部最优点通常满足一阶必要条件：

$$
\nabla f(x^*)=0
$$

如果 Hessian 矩阵正定：

$$
\nabla^2 f(x^*)\succ 0
$$

则 $x^*$ 是严格局部极小点。

## 10.3 Newton Method 的基本思想

在当前点 $x^{(k)}$ 附近，用二阶 Taylor 展开近似目标函数：

$$
f(x^{(k)}+d)\approx f(x^{(k)})+\nabla f(x^{(k)})^Td+\frac{1}{2}d^T\nabla^2 f(x^{(k)})d
$$

令该二次近似最小，可得 Newton 方向：

$$
d^{(k)}=-[\nabla^2 f(x^{(k)})]^{-1}\nabla f(x^{(k)})
$$

更新为：

$$
x^{(k+1)}=x^{(k)}+d^{(k)}
$$

或加入步长：

$$
x^{(k+1)}=x^{(k)}+\alpha_k d^{(k)}
$$

## 10.4 Newton Method 的优点

- 利用二阶曲率信息；
- 在最优点附近收敛很快；
- 对二次函数可以非常高效；
- 不需要像梯度下降那样沿谷底慢慢移动。

## 10.5 Newton Method 的缺点

- 需要计算 Hessian；
- 需要求解线性方程或矩阵逆；
- Hessian 不正定时 Newton 方向可能不是下降方向；
- 对初始点敏感；
- 在非凸问题中可能收敛到鞍点或局部极大点；
- 如果曲率接近 $0$，步长可能过大。

## 10.6 Levenberg-Marquardt Modification

Levenberg-Marquardt 方法可以理解为在 Newton 方法与 gradient descent 之间折中。常见思想是把 Hessian 修改为：

$$
\nabla^2 f(x)+\lambda I
$$

对应方向为：

$$
d=-[\nabla^2 f(x)+\lambda I]^{-1}\nabla f(x)
$$

当 $\lambda$ 很小时，接近 Newton method；当 $\lambda$ 很大时，方向更接近 gradient descent。

## 10.7 Line Search

在多维优化中，经常先确定方向 $d^{(k)}$，再确定步长 $\alpha_k$：

$$
x^{(k+1)}=x^{(k)}+\alpha_k d^{(k)}
$$

其中 $\alpha_k$ 可以通过一维优化确定：

$$
\alpha_k=\arg\min_{\alpha>0} f(x^{(k)}+\alpha d^{(k)})
$$

Line search 的作用是避免步长过大或过小。

## 10.8 一维搜索问题

若只知道函数值 $f(x)$，不知道函数表达式，并且已知最优解在 $[0,1]$ 内且函数单峰，则可以通过采样逐步缩小包含最优解的区间。

常见方法包括：

- uniform sampling；
- interval reduction；
- golden section search；
- derivative-based search；
- Newton method；
- secant method；
- chord method。

## 10.9 Golden Section Search

Golden section search 用于单峰函数的一维最小化。它通过选择两个内部点，使每次缩小区间后可以复用一个函数值，从而减少函数评价次数。

黄金比例相关参数为：

$$
\rho=\frac{\sqrt{5}-1}{2}
$$

其核心目标是在有限函数评价次数下尽快缩小最优点所在区间。

## 10.10 Momentum

在神经网络训练中，普通梯度下降为：

$$
w^{(t+1)}=w^{(t)}-\eta \nabla E(w^{(t)})
$$

加入 momentum 后：

$$
w^{(t+1)}=w^{(t)}-\eta \nabla E(w^{(t)})+\beta(w^{(t)}-w^{(t-1)})
$$

其中 $\beta$ 是动量系数。

Momentum 的正面效果是沿稳定方向加速，减少震荡；负面效果是可能由于惯性太强越过最优点。

## 10.11 Regularization

正则化把原目标函数：

$$
E(w)
$$

修改为：

$$
E(w)+\lambda \|w\|^2
$$

其中 $\lambda$ 控制正则化强度。

若 $\lambda$ 太小，约束不足，可能过拟合；若 $\lambda$ 太大，模型过于简单，可能欠拟合。

从多目标角度看，正则化相当于同时考虑两个目标：

$$
\min E(w)
$$

$$
\min \|w\|^2
$$

线性加权后得到：

$$
\min E(w)+\lambda \|w\|^2
$$

## 10.12 第10章复习要点

必须掌握：

- 一阶最优性条件；
- Newton method 的更新公式；
- Hessian 的作用；
- Newton method 为什么可能失败；
- line search 的含义；
- golden section search 的目的；
- momentum 的正负影响；
- regularization 与过拟合控制。

---

# 第11章 Quasi-Newton Methods and Conjugate Direction Methods

## 11.1 本章定位

课件中这一章材料较少，但课程大纲列出了 Quasi-Newton methods and conjugate direction methods。复习时需要掌握基本思想，尤其是它们与 Newton method、line search 的关系。

## 11.2 为什么需要 Quasi-Newton

Newton method 需要 Hessian：

$$
\nabla^2 f(x)
$$

以及求逆或求解线性系统。对于高维问题，这非常昂贵。Quasi-Newton 的思想是不直接计算真实 Hessian，而是利用迭代过程中的梯度变化近似 Hessian 或 Hessian 逆矩阵。

## 11.3 Quasi-Newton 基本形式

一般更新形式为：

$$
x^{(k+1)}=x^{(k)}+\alpha_k d^{(k)}
$$

其中方向为：

$$
d^{(k)}=-B_k^{-1}\nabla f(x^{(k)})
$$

$B_k$ 是 Hessian 的近似矩阵。

也可以直接近似 Hessian 逆：

$$
d^{(k)}=-H_k\nabla f(x^{(k)})
$$

其中 $H_k\approx [\nabla^2 f(x^{(k)})]^{-1}$。

## 11.4 Secant Condition

Quasi-Newton 更新通常满足 secant condition。定义：

$$
s_k=x^{(k+1)}-x^{(k)}
$$

$$
y_k=\nabla f(x^{(k+1)})-\nabla f(x^{(k)})
$$

则希望：

$$
B_{k+1}s_k=y_k
$$

这表示新的 Hessian 近似矩阵能够解释最近一次位移导致的梯度变化。

## 11.5 Conjugate Direction

共轭方向法的思想是选择一组方向，使它们相对于矩阵 $A$ 共轭。若方向 $d_i$ 和 $d_j$ 满足：

$$
d_i^T A d_j=0,\quad i\ne j
$$

则称它们关于 $A$ 共轭。

对于二次函数：

$$
f(x)=\frac{1}{2}x^TAx-b^Tx
$$

若 $A$ 正定，沿共轭方向搜索可以避免重复优化已经处理过的方向。

## 11.6 与 Gradient Descent 的区别

Gradient descent 每次沿负梯度方向走，可能在狭长谷底中反复震荡。共轭方向法通过构造不重复的搜索方向，提高二次问题上的收敛效率。

## 11.7 第11章复习要点

需要掌握：

- Quasi-Newton 为什么避免直接计算 Hessian；
- Hessian 近似矩阵 $B_k$ 或逆 Hessian 近似 $H_k$ 的含义；
- secant condition 的直观意义；
- 共轭方向与普通正交方向的区别；
- line search 在这类方法中的作用。

---

# 第12章 Nonlinear Optimization with Equality Constraints

## 12.1 本章定位

第12章讨论等式约束非线性优化。与无约束优化不同，解不能在整个空间中自由移动，而必须位于约束曲线或约束面上。

## 12.2 等式约束问题形式

基本模型为：

$$
\min f(x)
$$

$$
\text{subject to } h_i(x)=0,\quad i=1,2,\ldots,p
$$

其中 $h_i(x)=0$ 是等式约束。

## 12.3 可行域

可行域为：

$$
X=\{x\mid h_i(x)=0,\ i=1,2,\ldots,p\}
$$

优化只能在 $X$ 上进行。

即使某点满足：

$$
\nabla f(x)\ne 0
$$

它仍然可能是约束条件下的最优点，因为沿可行方向已经无法继续降低目标函数。

## 12.4 Lagrange Multiplier

对单个等式约束：

$$
\min f(x)
$$

$$
\text{subject to } h(x)=0
$$

构造 Lagrangian：

$$
L(x,\lambda)=f(x)+\lambda h(x)
$$

一阶必要条件为：

$$
\nabla_x L(x,\lambda)=\nabla f(x)+\lambda \nabla h(x)=0
$$

$$
h(x)=0
$$

其中 $\lambda$ 是 Lagrange multiplier。

## 12.5 几何意义

在等式约束最优点，目标函数等高线与约束曲线相切。因此 $\nabla f(x)$ 与 $\nabla h(x)$ 方向相关，可以写成：

$$
\nabla f(x)=-\lambda \nabla h(x)
$$

这表示目标函数梯度无法在可行曲线方向上继续下降。

## 12.6 多个等式约束

若存在多个等式约束：

$$
h_1(x)=0,\ h_2(x)=0,\ldots,h_p(x)=0
$$

则 Lagrangian 为：

$$
L(x,\lambda)=f(x)+\sum_{i=1}^{p}\lambda_i h_i(x)
$$

一阶条件为：

$$
\nabla f(x)+\sum_{i=1}^{p}\lambda_i\nabla h_i(x)=0
$$

$$
h_i(x)=0,\quad i=1,2,\ldots,p
$$

## 12.7 第12章复习要点

需要掌握：

- 等式约束优化形式；
- 可行域的含义；
- 约束最优点为什么不一定满足 $\nabla f(x)=0$；
- Lagrange multiplier 的公式；
- 等高线与约束曲线相切的几何解释。

---

# 第13章 Nonlinear Optimization with Inequality Constraints

## 13.1 本章定位

第13章讨论不等式约束非线性优化。不等式约束产生可行区域，最优点可能在区域内部，也可能在边界上。

## 13.2 不等式约束问题形式

一般模型为：

$$
\min f(x)
$$

$$
\text{subject to } g_i(x)\le 0,\quad i=1,2,\ldots,m
$$

也可以同时包含等式约束：

$$
h_j(x)=0,\quad j=1,2,\ldots,p
$$

## 13.3 Feasible Region

可行域为：

$$
X=\{x\mid g_i(x)\le 0,\ h_j(x)=0\}
$$

优化只能在可行域内进行。

## 13.4 Active Constraint

若在某点 $x$ 有：

$$
g_i(x)=0
$$

则该约束是 active constraint。

若：

$$
g_i(x)<0
$$

则该约束是 inactive constraint。

最优点在边界上时，通常会有一个或多个 active constraints。

## 13.5 KKT Conditions

对问题：

$$
\min f(x)
$$

$$
\text{subject to } g_i(x)\le 0,\quad i=1,2,\ldots,m
$$

构造 Lagrangian：

$$
L(x,\mu)=f(x)+\sum_{i=1}^{m}\mu_i g_i(x)
$$

KKT 条件包括：

### 1. Stationarity

$$
\nabla f(x)+\sum_{i=1}^{m}\mu_i\nabla g_i(x)=0
$$

### 2. Primal feasibility

$$
g_i(x)\le 0,\quad i=1,2,\ldots,m
$$

### 3. Dual feasibility

$$
\mu_i\ge 0,\quad i=1,2,\ldots,m
$$

### 4. Complementary slackness

$$
\mu_i g_i(x)=0,\quad i=1,2,\ldots,m
$$

## 13.6 Complementary Slackness 的意义

互补松弛条件表示：

- 如果约束不活跃，即 $g_i(x)<0$，则对应乘子必须为 $0$；
- 如果乘子 $\mu_i>0$，则约束必须活跃，即 $g_i(x)=0$。

因此，只有真正限制最优解的约束才会在 KKT 梯度平衡中发挥作用。

## 13.7 第13章复习要点

需要掌握：

- 不等式约束优化形式；
- feasible region 的含义；
- active constraint 与 inactive constraint；
- KKT 四类条件；
- complementary slackness 的直观含义；
- 为什么边界点可能是最优点。

---

# 第14章 Multi-objective Optimization: Basic Concepts

## 14.1 本章定位

第14章进入多目标优化。前面大多数问题只有一个目标，例如路径最短、成本最低、利润最大。但现实中很多问题有多个相互冲突的目标，例如：

- 成本低与质量高；
- 时间短与风险低；
- 误差小与模型复杂度低；
- 收益高与稳定性强。

多目标优化不再追求一个单一“最好”目标值，而是研究目标之间的权衡。

## 14.2 多目标优化模型

最大化形式：

$$
\max \big(f_1(x),f_2(x),\ldots,f_m(x)\big)
$$

$$
x\in X
$$

最小化形式：

$$
\min \big(f_1(x),f_2(x),\ldots,f_m(x)\big)
$$

$$
x\in X
$$

其中 $m$ 是目标数量。

## 14.3 Conflict

如果两个目标可以同时改善，则问题较简单。但多目标优化的核心在于目标冲突。即改善一个目标可能导致另一个目标变差。

例如正则化问题中：

$$
\min E(w)
$$

和：

$$
\min \|w\|^2
$$

通常存在冲突。训练误差越小，模型可能越复杂；模型越简单，训练误差可能越大。

## 14.4 Pareto Dominance

以最大化问题为例，解 $a$ 支配解 $b$，记为：

$$
a\prec b
$$

若满足：

$$
f_i(a)\ge f_i(b),\quad \forall i=1,2,\ldots,m
$$

并且至少存在一个目标 $j$，使得：

$$
f_j(a)>f_j(b)
$$

对于最小化问题，不等号方向相反。

## 14.5 Pareto Optimal Solution

如果不存在其他可行解支配 $x^*$，则 $x^*$ 是 Pareto optimal solution。

形式化地，对最大化问题：

$$
\nexists x\in X\text{ such that }x\text{ dominates }x^*
$$

Pareto 最优解不是唯一的，通常是一组解。

## 14.6 Pareto Set 与 Pareto Front

Pareto set 是决策空间中的 Pareto 最优解集合：

$$
PS=\{x\in X\mid x\text{ is Pareto optimal}\}
$$

Pareto front 是这些解映射到目标空间后的集合：

$$
PF=\{(f_1(x),f_2(x),\ldots,f_m(x))\mid x\in PS\}
$$

## 14.7 Non-dominated Solution Set

在有限候选解集合中，没有被其他候选解支配的解组成 non-dominated solution set。

这与 Pareto optimal 不完全相同。Pareto optimal 是相对于整个可行域而言；non-dominated set 通常是相对于当前有限样本而言。

## 14.8 多目标优化的目标

多目标优化通常希望找到一组解，使其：

- 接近真实 Pareto front；
- 在 Pareto front 上分布均匀；
- 覆盖范围广；
- 方便决策者选择。

## 14.9 随机点的支配概率

若在 $[0,1]^m$ 中随机生成两个点 $A$ 和 $B$，并考虑最大化问题，则 $B$ 支配 $A$ 的概率为：

$$
P(B\text{ dominates }A)=\left(\frac{1}{2}\right)^m
$$

因为每一个目标上 $B$ 优于 $A$ 的概率为 $\frac{1}{2}$，并且 $m$ 个目标独立。

随着 $m$ 增大，支配概率迅速降低。这解释了 many-objective optimization 中 Pareto dominance 选择压力下降的问题。

## 14.10 第14章实验重点

实验要求计算：

- 两个点在 $[0,1]^2$、$[0,1]^4$、$[0,1]^{10}$ 中的支配概率；
- 随机生成多个点时 non-dominated solutions 的期望数量；
- 目标维度越高，非支配解比例越高。

## 14.11 第14章复习要点

必须掌握：

- 多目标优化模型；
- 目标冲突；
- Pareto dominance；
- Pareto optimal solution；
- Pareto set 与 Pareto front；
- non-dominated solution set；
- 为什么目标数越多，支配关系越弱。

---

# 第15章 Search for a Single Final Solution in Multi-objective Optimization

## 15.1 本章定位

第15章讨论多目标优化中如何得到一个最终解。多目标问题通常有一组 Pareto 解，但实际决策往往需要选择一个方案。因此需要引入偏好信息。

## 15.2 Traditional Approach

传统方法是在优化前给定偏好，把多目标问题转化为单目标问题。

例如加权和方法：

$$
\max w_1f_1(x)+w_2f_2(x)+\cdots+w_mf_m(x)
$$

其中权重满足：

$$
w_i\ge 0,\quad \sum_{i=1}^{m}w_i=1
$$

## 15.3 Weighted Sum 方法

对于两目标最大化问题：

$$
\max f_1(x),f_2(x)
$$

可以转化为：

$$
\max w_1f_1(x)+w_2f_2(x)
$$

权重越大，表示对应目标越重要。

## 15.4 Weighted Sum 的局限

加权和方法简单，但存在明显局限。对于非凸 Pareto front，某些 Pareto optimal solutions 无法通过任何线性权重得到。

原因是线性加权等价于用一条直线或超平面去支撑 Pareto front。非凸区域中的点可能永远不会成为某个线性加权问题的最优解。

## 15.5 Reference Point 方法

决策者可以给出一个希望达到的目标点 $r$，算法寻找最接近该参考点的可行解。

例如可以最小化距离：

$$
\min \|F(x)-r\|
$$

其中：

$$
F(x)=(f_1(x),f_2(x),\ldots,f_m(x))
$$

## 15.6 A Posteriori Approach

另一类方法是先搜索一组 Pareto 解，再由决策者选择最终解。这是 EMO 中常见方式。

优点：

- 不需要提前给出准确偏好；
- 可以看到目标之间的 trade-off；
- 适合决策者不确定偏好的情况。

缺点：

- 计算量更大；
- 最终仍需要决策者从解集中选择。

## 15.7 第15章复习要点

需要掌握：

- 为什么多目标问题最终可能仍要选一个解；
- weighted sum 的公式和意义；
- 权重如何体现偏好；
- weighted sum 为什么不能找到所有 Pareto 解；
- reference point 的基本思想；
- traditional approach 与 EMO approach 的区别。

---

# 第16章 Search for Multiple Solutions in Multi-objective Optimization

## 16.1 本章定位

第16章是多目标优化的核心应用部分，主要讨论 Evolutionary Multi-objective Optimization，也就是 EMO。EMO 的目标不是只找一个解，而是在整个 Pareto front 上找到一组分布良好的解。

## 16.2 EMO 的两个目标

优秀的 EMO 算法需要同时满足：

### 1. Convergence

解集要接近真实 Pareto front。

### 2. Diversity

解集要在 Pareto front 上分布均匀，并尽可能覆盖整个 front。

如果只关注 convergence，可能所有解集中在 Pareto front 的一小段；如果只关注 diversity，解可能分散但远离 Pareto front。

## 16.3 Evolutionary Computation 基本流程

EMO 通常基于进化算法框架：

1. 初始化种群；
2. 计算每个个体的多个目标值；
3. 根据多目标评价方法选择优秀个体；
4. 使用 crossover 和 mutation 生成新个体；
5. 更新种群；
6. 重复迭代。

## 16.4 Solution-level Evaluation 与 Solution-set-level Evaluation

### Solution-level Evaluation

算法内部评价单个解，用于 selection。例如 Pareto rank、crowding distance、fitness 等。

### Solution-set-level Evaluation

评价整个算法最终得到的解集，用于算法比较。例如 HV、IGD、GD、spread 等。

## 16.5 Pareto Dominance-based Algorithms

这类算法用 Pareto dominance 排序个体。典型算法包括：

- MOGA；
- NPGA；
- NSGA；
- NSGA-II。

核心思想是：非支配解更好，被支配层数越低，优先级越高。

## 16.6 NSGA-II

NSGA-II 的主要机制包括：

### 1. Fast non-dominated sorting

把种群分成多个 front：

$$
F_1,F_2,\ldots
$$

$F_1$ 是非支配解集，$F_2$ 是去掉 $F_1$ 后的非支配解集，以此类推。

### 2. Crowding distance

在同一 front 内，用 crowding distance 维持多样性。拥挤距离越大，说明该解附近越稀疏，越应该保留。

### 3. Elitism

父代和子代合并后一起排序，保证优秀解不容易丢失。

## 16.7 Crowding Distance

对于每个目标，先按目标值排序，边界解拥挤距离设为无穷大，中间解根据相邻两个解的目标值差计算距离。

归一化形式为：

$$
CD_i=\sum_{j=1}^{m}\frac{f_j(i+1)-f_j(i-1)}{f_j^{\max}-f_j^{\min}}
$$

Crowding distance 的作用是保留分布较稀疏区域的解。

## 16.8 NSGA-II 的困难

当目标数增加时，很多解之间互不支配，导致 Pareto dominance 的选择压力下降。

此外，crowding distance 是按目标轴计算的，在三目标及以上问题中可能无法保证真实空间中的均匀分布。

这也是实验要求修改 NSGA-II generation update 机制的原因。

## 16.9 MOEA/D

MOEA/D 的核心是 decomposition。它把一个多目标问题分解为多个单目标子问题，每个子问题对应一个 weight vector。

常见分解方法包括：

### Weighted Sum

$$
\max \sum_{i=1}^{m}w_i f_i(x)
$$

### Tchebycheff

$$
\min \max_{1\le i\le m} w_i |f_i(x)-z_i^*|
$$

其中 $z^*$ 是理想点。

### PBI

PBI 同时考虑沿权重方向的收敛距离和垂直于权重方向的偏离距离。

MOEA/D 的优势是可以通过均匀设置 weight vectors 来引导解集分布。

## 16.10 Indicator-based Algorithms

Indicator-based algorithms 使用性能指标指导选择，例如 hypervolume。

SMS-EMOA 是典型例子。其基本思想是：当需要删除一个解时，删除 hypervolume contribution 最小的解。

某个解 $x$ 的 HV contribution 可以表示为：

$$
\Delta HV(x)=HV(S)-HV(S\setminus\{x\})
$$

贡献越小，说明删除它对整体 HV 影响越小。

## 16.11 Many-objective Optimization

当目标数量较多时，会出现：

- 大量解互不支配；
- Pareto rank 区分能力下降；
- 可视化困难；
- HV 计算成本高；
- reference point 或 weight vector 设计困难；
- 解集规模需要更大才能覆盖 front。

因此 many-objective optimization 需要额外机制，例如 reference vector、indicator、dimension reduction 或 preference-based methods。

## 16.12 第16章实验重点

实验给定 14 个网格点，要求：

1. 用 NSGA-II 选择 7 个解；
2. 用自己的想法选择 7 个更均匀分布的解；
3. 修改 NSGA-II 的 generation update 机制，使选择结果更均匀；
4. 思考三目标及以上时 crowding distance 为什么不够好；
5. 设计新的距离或选择机制。

## 16.13 第16章复习要点

必须掌握：

- EMO 的目标是找到一组 well-distributed solutions；
- convergence 与 diversity 的区别；
- NSGA-II 的排序、拥挤距离、精英保留；
- crowding distance 的计算思想；
- NSGA-II 在 many-objective 中的问题；
- MOEA/D 的 decomposition 思想；
- SMS-EMOA 与 HV contribution；
- 为什么多目标算法评价的是解集而不是单个解。

---

# 第16章补充：Performance Indicators for EMO

## 17.1 本章定位

这一部分虽然对应后续课件，但内容上是第16章的延伸：如何评价 EMO 得到的 solution set。单目标优化最终得到一个解，多目标优化最终得到一组解，因此评价难度更高。

## 17.2 单目标与多目标评价差异

单目标优化中，算法性能通常等于最终解的性能。若目标是最小化，比较两个解只需看：

$$
f(x_1)<f(x_2)
$$

多目标优化中，最终结果是解集 $S$，因此需要比较两个解集：

$$
S_A\quad \text{vs.}\quad S_B
$$

这通常不能只用一个目标值判断。

## 17.3 Performance Indicator

Performance indicator 是把一个解集映射成数值的函数：

$$
I(S)\in \mathbb{R}
$$

用于比较不同算法或不同解集。

好的指标通常关注：

- convergence；
- diversity；
- spread；
- uniformity；
- Pareto compliance；
- 计算成本；
- 对 reference point 或 reference set 的依赖。

## 17.4 GD

Generational Distance 衡量得到的解集到真实 Pareto front 的平均距离。若 $S$ 是算法得到的解集，$PF$ 是真实 Pareto front，则：

$$
GD(S)=\frac{1}{|S|}\left(\sum_{x\in S}d(x,PF)^p\right)^{1/p}
$$

GD 越小，表示解集越接近 Pareto front。

## 17.5 IGD

Inverted Generational Distance 从参考点集到解集计算距离。若 $R$ 是 Pareto front 上均匀采样的参考点集，则：

$$
IGD(S)=\frac{1}{|R|}\sum_{r\in R}d(r,S)
$$

其中：

$$
d(r,S)=\min_{x\in S}\|r-F(x)\|
$$

IGD 同时反映 convergence 和 diversity，但依赖参考点集 $R$ 的质量。

## 17.6 IGD+

IGD+ 是 IGD 的改进版本，试图修正 IGD 在 Pareto compliance 方面的问题。其距离计算只惩罚在目标方向上不好的部分。

对于最小化问题，常见形式为：

$$
d^+(r,a)=\sqrt{\sum_{i=1}^{m}\max(a_i-r_i,0)^2}
$$

## 17.7 Epsilon Indicator

Epsilon indicator 衡量一个解集需要平移多少才能弱支配另一个解集。

对于最小化问题，加性 epsilon indicator 可以理解为寻找最小的 $\epsilon$，使得对参考集中每个点，都存在算法解在每个目标上不比它差超过 $\epsilon$。

## 17.8 Hypervolume

Hypervolume 衡量解集相对于 reference point 所支配区域的体积。对于最大化问题，reference point 应该比所有解都差。

若解集为 $S$，参考点为 $r$，则：

$$
HV(S)=\text{Volume}\left(\bigcup_{x\in S}[r_1,f_1(x)]\times\cdots\times[r_m,f_m(x)]\right)
$$

HV 越大，通常表示解集越好。

## 17.9 Reference Point 的影响

HV 对 reference point 非常敏感。不同 reference point 可能导致不同解集排序。

因此使用 HV 时必须明确：

- reference point 的位置；
- 所有算法是否使用同一个 reference point；
- 目标是否归一化；
- 是最大化问题还是最小化问题。

## 17.10 Pareto Compliance

若解集 $A$ 支配解集 $B$，一个 Pareto compliant 指标应当给 $A$ 更好评价。

HV 通常具有较好的 Pareto compliance 性质，因此在 EMO 中非常重要。

## 17.11 Diversity 指标

常见 diversity 指标包括：

- spread；
- maximum spread；
- spacing；
- Deb's spread；
- crowding distance；
- coverage。

它们关注解集是否覆盖范围广、是否均匀。

## 17.12 公平比较问题

比较不同 EMO 算法时，需要注意：

- 种群大小是否相同；
- 函数评价次数是否相同；
- 最终解集大小是否相同；
- 是否使用相同 reference point；
- 是否进行归一化；
- 是否多次独立运行并统计平均结果。

如果一个算法输出 1000 个解，另一个输出 100 个解，直接比较 HV 可能不公平。因此课件强调，最好从所有搜索到的解中选择相同数量的解再比较。

## 17.13 Indicators Lab 重点

实验给定问题：

$$
\max f_1(x)=x_1,\quad f_2(x)=x_2
$$

$$
\text{subject to } x_1+x_2\le 1,\quad x_1\ge 0,\quad x_2\ge 0
$$

Pareto front 是连接 $(0,1)$ 与 $(1,0)$ 的线段：

$$
x_1+x_2=1,\quad x_1,x_2\ge 0
$$

实验要求分析不同 reference point 下，单个解、两个解、五个解如何最大化 HV，以及当参考点均匀分布在 Pareto front 上时，五个解如何最小化 IGD。

## 17.14 第17部分复习要点

必须掌握：

- 为什么多目标算法评价 solution set；
- GD 与 IGD 的区别；
- HV 的定义；
- reference point 对 HV 的影响；
- Pareto compliance 的含义；
- 为什么公平比较要控制解集大小和函数评价次数；
- 指标选择会影响算法比较结论。

---

# 全课程复习总纲

## 一、按知识线索理解

整门课可以分成四条主线。

### 1. 组合优化启发式

包括：

- greedy；
- local search；
- VNS；
- SA；
- TS；
- EA；
- subset selection。

核心问题是：可行解离散且数量巨大，不能穷举，只能在有限时间内找高质量近似解。

### 2. 数学规划

包括：

- LP；
- Simplex；
- ILP；
- LP relaxation；
- Branch and Bound。

核心问题是：如何用数学模型和 solver 精确或近似求解结构化优化问题。

### 3. 非线性优化

包括：

- gradient descent；
- line search；
- Newton method；
- Quasi-Newton；
- equality constraints；
- inequality constraints；
- KKT。

核心问题是：如何利用导数、梯度、Hessian 和约束条件寻找连续空间中的最优解。

### 4. 多目标优化

包括：

- Pareto dominance；
- Pareto optimality；
- Pareto front；
- weighted sum；
- EMO；
- NSGA-II；
- MOEA/D；
- HV；
- IGD。

核心问题是：多个目标相互冲突时，如何找到一组能体现 trade-off 的解。

## 二、最重要的公式汇总

### TSP 对称 tour 数

$$
\frac{(n-1)!}{2}
$$

### 0-1 背包

$$
\max \sum_{i=1}^{n}v_i x_i
$$

$$
\text{subject to } \sum_{i=1}^{n}w_i x_i\le W
$$

$$
x_i\in\{0,1\}
$$

### 梯度下降

$$
x^{(k+1)}=x^{(k)}-\alpha_k\nabla f(x^{(k)})
$$

### Newton Method

$$
x^{(k+1)}=x^{(k)}-[\nabla^2 f(x^{(k)})]^{-1}\nabla f(x^{(k)})
$$

### Line Search

$$
x^{(k+1)}=x^{(k)}+\alpha_k d^{(k)}
$$

### Lagrange 条件

$$
\nabla f(x)+\lambda \nabla h(x)=0
$$

$$
h(x)=0
$$

### KKT 条件

$$
\nabla f(x)+\sum_{i=1}^{m}\mu_i\nabla g_i(x)=0
$$

$$
g_i(x)\le 0
$$

$$
\mu_i\ge 0
$$

$$
\mu_i g_i(x)=0
$$

### Pareto dominance 最大化

$$
f_i(a)\ge f_i(b),\quad \forall i
$$

且至少存在一个 $j$：

$$
f_j(a)>f_j(b)
$$

### Crowding distance

$$
CD_i=\sum_{j=1}^{m}\frac{f_j(i+1)-f_j(i-1)}{f_j^{\max}-f_j^{\min}}
$$

### IGD

$$
IGD(S)=\frac{1}{|R|}\sum_{r\in R}\min_{x\in S}\|r-F(x)\|
$$

### Hypervolume

$$
HV(S)=\text{Volume}\left(\bigcup_{x\in S}[r_1,f_1(x)]\times\cdots\times[r_m,f_m(x)]\right)
$$

## 三、最容易出问答题的点

1. 为什么 greedy 不一定最优？
2. 为什么 greedy solution 仍然有用？
3. local solution 和 global solution 有什么区别？
4. 为什么 local optimum 依赖 neighborhood structure？
5. first move 和 best move 哪个更好？
6. VNS/VND 为什么能改善 local search？
7. SA 为什么能跳出局部最优？
8. TS 与 SA 有什么区别？
9. EA 为什么是 population-based search？
10. LP 和 ILP 有什么区别？
11. LP relaxation 有什么用？
12. 为什么 gradient descent 的步长很重要？
13. Newton method 为什么可能失败？
14. 约束优化中为什么不一定有 $\nabla f(x)=0$？
15. Pareto dominance 是什么？
16. 为什么多目标优化不能简单说哪个解最好？
17. NSGA-II 如何同时考虑 convergence 和 diversity？
18. many-objective optimization 为什么困难？
19. HV 为什么依赖 reference point？
20. 为什么 EMO 算法比较要控制解集大小和函数评价次数？

## 四、实验复习建议

实验题通常不是单纯背诵，而是要求你解释、构造、比较或提出自己的想法。复习时要特别注意：

- 能构造 greedy 失败的例子；
- 能计算 TSP 邻域大小；
- 能说明不同邻域对 local search 的影响；
- 能比较 SA 的不同 cooling schedule；
- 能解释 tournament selection 概率；
- 能比较不同 generation update 机制；
- 能提出巨大候选集下加速 greedy 的思路；
- 能区分 LP solver、ILP solver、LP relaxation；
- 能画梯度下降路径并解释步长影响；
- 能判断 Pareto dominance；
- 能用 HV、IGD 解释解集质量。

---

# 课程整体逻辑图

```text
Introduction
    ↓
Greedy Algorithm
    ↓
Local Search and Neighborhood
    ↓
VNS / SA / TS / EA
    ↓
Subset Selection and Branch & Bound
    ↓
LP / Simplex / ILP
    ↓
Gradient Descent / Newton / Constraint Optimization
    ↓
Multi-objective Optimization
    ↓
EMO / NSGA-II / MOEA/D / Indicators
```

整门课的核心不是记住每个算法名字，而是理解不同算法如何在以下矛盾之间做平衡：

- 解质量 vs 计算时间；
- 局部搜索 vs 全局探索；
- 精确最优 vs 近似可行；
- 单一目标 vs 多目标权衡；
- 算法通用性 vs 问题特定设计；
- 理论保证 vs 实际表现。
