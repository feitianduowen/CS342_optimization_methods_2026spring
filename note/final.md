## 第1章 Introduction

**优化方法导论**
**对应课件：2026-01-Introduction-Students；实验：2026-01-Lab Session**

这一章主要是建立“什么是优化问题、为什么要学优化、优化和机器学习有什么关系、不同优化问题如何分类”的整体框架。

### 需要掌握的知识点

1. **Optimization problem 优化问题的基本含义**
   优化就是在所有可行解中寻找最好的解。一般包括：
   - 决策变量：要决定什么；
   - 目标函数：要最大化或最小化什么；
   - 约束条件：解必须满足什么限制；
   - 可行解：满足约束的解；
   - 最优解：目标函数值最好的可行解。
2. **Learning and Optimization 的关系**
   课件用神经网络学习举例：学习可以看成调整连接权重，使训练数据上的误差函数最小。也就是说，learning 在形式上可以看作 optimization。
3. **学习和优化的区别**
   二者虽然都在最小化损失函数，但最终目标不同：
   - learning 更关注 testing data accuracy，即对未知测试数据的泛化能力；
   - optimization 更关注 training data accuracy，即给定目标函数上的最优值。
4. **训练误差与测试误差**
   课件中给出训练数据$x_1,y_1$,$\ldots,(x_m,y_m)$，测试数据 $(x_{m+1},y_{m+1}),\ldots$。训练时最小化训练误差，评价学习效果时看测试误差。
5. **Neural Architecture Search 是否属于优化**
   课件提出问题：NAS 是 learning 还是 optimization？你要理解：它既与学习有关，因为目标是获得泛化能力好的模型；也明显是优化问题，因为要搜索网络结构和权重，使某种评价指标最好。
6. **优化问题的分类**
   需要会从几个角度分类：
   - 连续优化 vs 离散/组合优化；
   - 单目标优化 vs 多目标优化；
   - 无约束优化 vs 有约束优化；
   - 线性优化 vs 非线性优化；
   - 精确算法 vs 近似/启发式算法。
7. **Local solution 与 Global solution**
   - Local solution：在它的邻域内没有更好的解；
   - Global solution：在全部可行解中最好的解。
     课件中特别强调，一个问题可以有多个全局最优解。
8. **Approximate solution 与 Near-optimal solution**
   Approximate solution 是由近似算法得到的解，可能很差，也可能很好，甚至可能正好是最优解；Near-optimal solution 通常指目标函数值接近最优值的好解，但“near”没有特别严格统一的数学定义。
9. **Multi-modal optimization 多峰优化**
   当一个问题有多个全局最优解时，可以称为 multi-modal optimization。此时算法目标可能不只是找一个最优解，而是找出多个全局最优解，甚至包括一些局部最优解。
10. **实验部分要掌握的问题规模计算**
    第1周实验要求你用 PPT 解释问题规模。重点包括：

- n-city TSP 不同路径数不是$n!$，因为循环移位和反向路径会被视为相同；
- 对称 TSP 的不同 tour 数通常是$(n-1)!/2$；
- 3-machine 4-job load balancing 中机器相同，因此本质是把4个 job 分成最多3组；
- 2-machine n-job load balancing 也不能简单看作普通子集选择，因为两台机器相同，互换机器不产生新解。

这一章最重要的是：**明确优化问题的基本构成，并理解“学习可以看作优化，但学习最终更强调泛化”。**

------

## 第2章 Greedy algorithms for combinatorial optimization

**组合优化中的贪心算法**
**对应课件：2026-02-Greedy and Introduction Students；实验：2026-02-Lab Session**

这一章重点是：**贪心算法每一步做当前看来最好的选择，但最终结果不一定全局最优。**

### 需要掌握的知识点

1. **Greedy algorithm 的基本思想**
   贪心算法在每一步都选择当前局部最优的操作，不回头修改之前的选择。它通常简单、快速，但不一定能得到最优解。
2. **TSP 中的 Nearest Neighbor Greedy Method**
   对 TSP，课件给出的 nearest neighbor greedy method 是：
   - 任意选择一个起始城市；
   - 每次从当前城市移动到剩余城市中最近的城市；
   - 直到访问所有城市后回到起点。
     课件明确指出，很多情况下这种 greedy solution 不是最优的。
3. **TSP 的基本建模**
   TSP 的输入是$n$个城市以及城市间距离$d_{ij}=d_{ji}$，目标是找到一条访问所有城市并回到起点的最短 tour。
4. **为什么 greedy solution 可能不好**
   贪心只看当前一步最近或收益最高的选择，可能导致后面必须付出很大代价。例如 TSP 中前面选了局部最近城市，最后可能产生很长的回程边。
5. **Greedy solution 可以被局部搜索改进**
   课件指出，很多情况下 greedy tour 可以通过 small changes 得到更好的 tour，这也是后面把 local search 用在 greedy tour 上的主要动机。
6. **TSP 中交叉边说明 tour 非最优**
   如果欧氏 TSP 的 tour 中有两条边相交，那么该 tour 通常不是最优的；通过交换边可以得到更短路径。课件用虚线红边说明修改后的 tour 更短。
7. **Knapsack 中 greedy 的失败**
   实验要求你构造一个背包问题例子，说明 greedy solution 可以远差于 optimal solution，甚至 greedy 总利润可以小于最优总利润的 $1/100$。
8. **TSP 中 greedy 的失败**
   实验要求构造一个 TSP 例子，说明 greedy tour length 可以超过 optimal tour length 的两倍。
9. **Load balancing 中 greedy 的失败**
   实验要求构造一个 load balancing 例子，说明 greedy makespan 可以接近最优 makespan 的两倍。这里的 makespan 是所有机器完成任务时间中的最大值。
10. **Greedy 的优缺点总结**
    优点是简单、速度快、容易实现，适合生成初始解；缺点是缺乏全局视野，可能被局部选择误导。

这一章最重要的是：**会用具体反例说明 greedy 不一定好，而不是只会说“贪心不一定最优”。**

------

## 第3章 LS and neighborhood structures for combinatorial optimization

**局部搜索与邻域结构**
**对应课件：2026-03-Local Search-Students；实验：2026-03-Lab Session**

这一章前面我已经整理过一部分，这里结合你新上传的第3周课件再补全。重点是：**从 greedy solution 出发，通过小修改不断改进当前解。**

### 需要掌握的知识点

1. **Local Search 的基本机制**
   课件给出的基本流程是：
   - 对当前 tour 做一个小修改；
   - 如果修改后更好，就接受；
   - 如果没有改进，就不接受；
   - 继续检查其他修改。
2. **为什么从 greedy tour 开始做 LS**
   Greedy tour 往往不是最优，但通常比随机 tour 好。因此可以先用 greedy 快速得到一个初始解，再用 local search 对它进行改进。
3. **Neighborhood structure 邻域结构**
   邻域结构决定“什么叫小修改”。不同邻域结构会导致不同搜索能力和不同计算成本。
4. **TSP 常见邻域结构**
   实验要求计算以下邻域结构在 n-city TSP 中产生的邻居数量：
   - Adjacent Two-City Change；
   - Arbitrary Two-City Change；
   - Insertion / Shift；
   - Inversion / Arbitrary Two-Edge Change；
   - Arbitrary Three-City Change。
     要求答案必须是含$n$的公式，而不是只写某个具体数值。
5. **Adjacent Two-City Change**
   只交换相邻两个城市，邻域小，计算快，但改进能力有限。
6. **Arbitrary Two-City Change**
   任意选两个城市交换位置，包含相邻交换，邻域比 adjacent two-city change 更大。
7. **Insertion / Shift**
   取出一个城市，插入到 tour 中另一个位置。它适合调整某个城市在路径中的相对位置。
8. **Inversion / Two-Edge Change**
   选取路径中的一段并反转顺序，相当于改变两条边。它在 TSP 中非常重要，因为可以消除交叉边、缩短路径。
9. **Arbitrary Three-City Change**
   允许同时改变三个城市的位置，邻域更大，可能找到更好的改进，但计算量也更高。
10. **邻域大小与计算量的关系**
    邻域越大，每一步需要检查的候选解越多，计算量越高；邻域越小，搜索快但容易陷入局部最优。
11. **Local optimal solution 依赖于邻域定义**
    同一个解，在小邻域下可能是 local optimal solution；但在大邻域下可能还能被改进。课件特别强调，局部最优解的定义依赖于 neighborhood structure。
12. **Local solution 与 Global solution 的区别**
    Local solution 只是在当前邻域内没有更好解；Global solution 是所有可行解中最优。局部搜索停止时得到的通常只是 local solution，不保证 global solution。
13. **交叉边与 inversion 的关系**
    对欧氏 TSP，如果当前 tour 中两条边相交，可以通过 inversion 或 two-edge change 消除交叉，从而得到更短 tour。这个思想是 TSP 局部搜索中非常常见的判断方法。
14. **实验中最可能考的内容**
    这一章实验不是让你跑程序，而是让你推导不同邻域结构的邻居数量公式。重点是要会解释：

- 先确定一次 move 需要选择几个位置；
- 是否区分顺序；
- 是否包含重复或无效操作；
- 是否把环形 tour 中等价路径视为相同。

这一章最重要的是：**会根据邻域结构推导邻居数量，并理解“邻域不同，局部最优也不同”。**

------

## 第1—3章复习重点汇总

这三章主要是整门课的基础，建议你按下面顺序掌握：

| 优先级 | 内容                       | 必须掌握到什么程度                                         |
| ------ | -------------------------- | ---------------------------------------------------------- |
| 最高   | 优化问题基本构成           | 会说清变量、目标函数、约束、可行解、最优解                 |
| 最高   | Greedy algorithm           | 会解释原理，并能举反例说明 greedy 可能很差                 |
| 最高   | TSP 基本概念               | 会写输入、目标、输出；知道 tour 等价导致不是 (n!)          |
| 高     | Local Search               | 会写基本流程，知道从当前解找邻居解                         |
| 高     | Neighborhood structure     | 会区分 adjacent swap、arbitrary swap、insertion、inversion |
| 高     | Local vs Global            | 会解释局部最优不等于全局最优                               |
| 中     | Approximate / Near-optimal | 会区分 approximate solution 和 near-optimal solution       |
| 中     | 实验题                     | 会构造 greedy 失败例子，会推导 TSP 邻居数量                |

## 第3章 LS and neighborhood structures for combinatorial optimization

**局部搜索与邻域结构**
**对应课件：2026-04-LS-VNS-Students；实验：2026-04-Lab Session**

这一章的核心是：**给定一个初始解，通过邻域结构不断寻找更好的邻居解，直到无法改进为止。**

需要掌握的知识点：

1. **Local Search 局部搜索基本思想**
   从一个初始解出发，在它的邻域中寻找更优解；如果找到更优解，就移动到该解；如果所有邻居都不能改进，就停止。停止时得到的是**局部最优解**，不一定是全局最优解。
2. **Neighborhood structure 邻域结构**
   邻域结构决定“当前解附近有哪些候选解”。例如 TSP 中常见的邻域是 **2-edge change / inversion**，也就是把路径中一段顺序反转。实验中明确使用 inversion 作为 TSP 的邻域结构。
3. **First Move 与 Best Move**
   - **First Move**：找到第一个能改进的邻居就移动，计算量较小；
   - **Best Move**：检查所有邻居，选择改进最大的那个，计算量较大。
     课件强调：一般来说 first move 计算负担更小，但最终解质量无法简单判断哪个一定更好。
4. **局部最优的局限**
   局部搜索可能陷入 local solution，即当前邻域内没有更优解，但全局上还有更好的解。
5. **初始解的重要性**
   不同初始解可能收敛到不同局部最优。实验中要求第一个初始解用 greedy solution，之后的初始解需要自己设计生成方式。
6. **实验要会做的内容**
   实验要求你构造一个 TSP 问题，使得从某个初始城市得到的 greedy solution 不是最优解，而且不能被 inversion-based local search 改进；还要求设计 knapsack problem 的多个邻域结构 $N_1,N_2,N_3,\ldots$。

这一章最重要的是：**会解释“解—邻域—移动—局部最优”的关系，并能判断 first move 和 best move 的优缺点。**

------

## 第4章 Variable Neighborhood Search, VND, SA, TS, EC

**变邻域搜索、模拟退火、禁忌搜索、进化计算**
**对应课件：2026-04-LS-VNS-Students、2026-05-SA-TS-Students、2026-06-TS-EA-Students**

这一章内容比较多，可以分成四组：**VNS/VND、SA、TS、EA/EC**。

------

### 4.1 Variable Neighborhood Search, VNS

**变邻域搜索**

VNS 的核心思想是：**不要只用一个邻域，而是使用多个不同规模或不同类型的邻域。** 小邻域搜索快但容易陷入局部最优，大邻域搜索范围广但计算量大，所以需要平衡。

需要掌握：

1. **为什么需要 VNS**
   普通局部搜索只在固定邻域里找改进，容易卡在局部最优。VNS 通过改变邻域结构，尝试跳出当前局部最优。
2. **多个邻域结构 $N_1,N_2,\ldots,N_{kmax}$**
   课件中说明，通常 $N_{k+1}$ 比 $N_k $更大，有时也可以理解为 $N_k \subset N_{k+1}$。搜索时先用 $N_1$，再用 $N_2,N_3,\ldots$。
3. **TSP 中的邻域例子**
   对 n-city TSP，可以设计 $k$-edge change neighborhood，例如 2-edge、3-edge、4-edge change。

------

### 4.2 Variable Neighborhood Descent, VND

**变邻域下降法**

VND 可以看成 VNS 的一个变体。它不是随机扰动，而是依次使用不同邻域做局部改进。

需要掌握：

1. **VND 的流程**
   从 $N_1 $开始做 best move local search；如果没有改进，就切换到 $N_2$；再没有改进就继续到 $N_3$。
2. **VND 与普通 LS 的区别**
   普通 LS 使用一个固定邻域；VND 使用多个邻域，因此更有机会突破某个邻域下的局部最优。
3. **实验中的 knapsack 邻域设计**
   例如可以设计：
   - $N_1$：翻转一个物品的选择状态；
   - $N_2$：删除一个物品并加入另一个物品；
   - $N_3$：交换两个或多个物品；
   - $N_4$：随机移除若干物品再重新填充。

------

### 4.3 Simulated Annealing, SA

**模拟退火**

SA 的核心思想是：**允许接受较差解，从而跳出局部最优。** 课件把它和 TS 一起归为“allow the move to a worse solution”的方法，而 LS、ILS、VNS 主要是“move to a better solution”。

需要掌握：

1. **为什么 SA 可以跳出局部最优**
   因为它不是只接受更好解，也会以一定概率接受更差解。
2. **温度 Temperature 的含义**
   - 高温：更容易接受较差解，搜索范围广；
   - 低温：更少接受较差解，更像局部搜索。
3. **Cooling Schedule 冷却策略**
   实验要求比较多种温度策略：恒定高温、恒定低温、恒定中温、快速降温、慢速降温。
4. **接受劣解的概率**
   通常与目标函数变差程度和温度有关。温度越高，接受差解概率越大；温度越低，越接近贪心式局部搜索。
5. **实验中的 knapsack 问题**
   实验是 100-item knapsack，有 10 个约束，解是长度为100的二进制向量；邻居用 Hamming distance $D=1,2,3 $定义，并限制 1000 次 solution evaluations。
6. **约束处理 Constraint Handling**
   实验中可以用：
   - **Repair**：如果解不可行，就删除物品直到可行；
   - **Penalty**：如果解不可行，就给目标函数加惩罚项。

------

### 4.4 Tabu Search, TS

**禁忌搜索**

TS 的核心思想是：**允许移动到较差解，但用 tabu list 避免搜索马上回到刚才的解或重复循环。**

需要掌握：

1. **Tabu List 禁忌表**
   记录最近访问过的解、操作或特征，防止搜索在同一区域反复循环。
2. **TS 与 SA 的区别**
   SA 主要依靠温度和概率控制是否接受较差解；TS 依靠 tabu list 控制搜索方向。课件中还提到，SA 通常需要提前知道可用计算时间，而 TS 不一定需要。
3. **TS 的优势与困难**
   优势是通用性强、在很多局部最优较多的问题上比普通 LS 表现更好；困难是 tabu list 的设计通常需要对问题有较深理解，初始解也很重要。
4. **什么时候适合 TS**
   当已有一个较好的初始解，并希望在其附近进行较细致搜索时，TS 比较合适。课件中也提到：SA 更像是在早期寻找有希望区域，TS 更像是从好初始解出发仔细搜索。

------

### 4.5 Evolutionary Algorithms / Evolutionary Computation

**进化算法 / 进化计算**

EA 的核心思想是：**不是从一个解出发，而是同时维护一组解，即 population-based search / multi-point search。** 课件中明确把进化算法称为 population-based 和 multi-point search algorithms。

需要掌握：

1. **Population 种群**
   同时保留多个候选解，而不是只保留当前一个解。
2. **Selection 选择**
   更好的解更容易被选中，后代通常从较好的解中产生。课件中强调 EA 会 focus on better solutions，并从 better solutions 生成新解。
3. **Mutation 变异**
   随机选择一个邻居，相当于对当前解进行小扰动。
4. **Crossover 交叉**
   从两个父代中重组信息，生成新解。课件将 mutation 和 crossover 列为生成新解的两个主要算子。
5. **Tournament Selection 锦标赛选择**
   随机选 $K $个解，从中选最好的作为父代。$K $越大，选择压力越大；$K=1 $时相当于随机选择。
6. **GA、ES、EP 的区别**
   课件中区分了：
   - **ES**：常用于实数编码、函数优化；
   - **EP**：早期常用于有限自动机；
   - **GA**：常用 mutation 和 crossover，可处理二进制串、整数、排列、树等编码。
7. **Generation Update 代更新机制**
   实验中要求比较多种 ES 更新机制，例如 $(1,1 )$ES、 $(1+1 )$ES、 $(1+\lambda )$ES、 $(\mu+1 )$ES、 $(\mu,\mu )$ES、 $(\mu+\mu )$ES、 $(\mu,\lambda )$ES。重点不是死记名字，而是理解“父代是否保留”“每代产生多少子代”“选择压力多大”。

这一章最重要的是：**理解全局探索 wide global search 与局部高效搜索 focused efficient search 的平衡。** 课件明确指出，优化算法设计的目标就是在这两者之间找到合适平衡。

------

## 第5章 Branch and Bound algorithms, and subset selection algorithms

**分支定界与子集选择算法**
**对应课件：2026-08-Subset Selection Students；实验：2026-08-Lab Session**

这一章重点是 **Subset Selection Problems**，也就是从候选集合里选出一个子集，使目标函数最好，并满足约束。

需要掌握的知识点：

1. **子集选择问题的基本形式**
   输入是候选集合：
   $$
   S_C={s_1,s_2,\ldots,s_n}
   $$
   输出是被选中的子集 $S\subseteq S_C$。目标可以是最大化或最小化 $f(S )$，约束可以是 $g(S)=G $或 $g(S)\le G$。
2. **Knapsack Problem 背包问题**
   背包问题是典型子集选择问题。每个物品有价值 $v_i $和重量 $w_i$，决策变量 $x_i\in{0,1}$，目标是最大化总价值，同时满足容量约束。
3. **固定选择数量的子集选择**
   最简单版本是要求：
   $$
   |S|=k
   $$
   即从 $n $个候选项中选 $k $个。搜索空间大小是组合数，通常为：
   $$
   {n\choose k}
   $$
   当 $n $很大时，穷举不可行。
4. **Hypervolume Subset Selection**
   课件用多目标优化中的 hypervolume subset selection 做例子：从候选点中选 $k $个，使它们的 HV 最大。这个例子用来说明子集选择的搜索空间很大，而且不同子集的质量需要通过目标函数评价。
5. **Greedy Algorithm 贪心选择**
   每一步选择当前看起来最好的元素。优点是快，缺点是可能不是全局最优。
6. **Local Improvement 局部改进**
   在已有子集基础上，尝试添加、删除或交换元素，改进当前解。
7. **巨大候选集下的计算问题**
   实验中特别提到，当候选集非常大，例如 5 亿个 items 时，贪心算法每一步都检查全部候选项会非常慢；随机选择一个 item 做局部改进也可能低效。因此要设计近似筛选、采样、候选池、分层搜索等方法来降低计算时间。
8. **Branch and Bound 分支定界**
   虽然你这次上传的第8讲更偏 subset selection，但课程大纲中第5章也包含 branch and bound。复习时要掌握：
   - Branch：把问题拆成子问题；
   - Bound：计算子问题可能达到的最好界；
   - Prune：如果某个子问题不可能优于当前最好解，就剪枝。

这一章考试可能问：**为什么子集选择难？为什么 greedy 快但不一定最优？候选集很大时如何减少计算量？**

------

## 第6章 Linear programming problem formulations and applications

**线性规划建模与应用**
**对应课件：2026-09-LP and ILP for Students；实验：2026-09-Lab Session**

这一章重点是会把文字问题写成 LP 模型。

需要掌握的知识点：

1. **LP 的标准结构**
   线性规划要求目标函数和约束条件都是线性的。课件给出的形式包括：
   $$
   \max c^T x
   $$
   subject to：
   $$
   Ax=b,\quad x\ge 0
   $$
   或：
   $$
   Ax\le b,\quad x\ge 0
   $$
2. **决策变量 Decision Variables**
   先定义“要决定什么”。例如混凝土问题中，要决定购买多少磅第一种混凝土和第二种混凝土。
3. **目标函数 Objective Function**
   明确是最大化利润、最小化成本，还是其他目标。
4. **约束 Constraints**
   把资源限制、需求限制、比例要求等写成线性不等式或等式。
5. **非负约束 Non-negativity**
   很多实际问题中 $x_i\ge 0$，因为数量、重量、金额不能为负。
6. **建模例子：混凝土配比问题**
   课件中给出两种混凝土，每种含有不同比例的 cement、gravel、sand，成本不同，要求用最小成本满足材料需求。这类题重点是把文字转化为 $c^Tx$、$Ax\ge b$、$x\ge 0$。

这一章最重要的是：**会从题目中找变量、目标、约束，并写成矩阵形式。**

------

## 第7章 Linear programming algorithms

**线性规划算法**
**对应课件：2026-09-LP and ILP for Students；实验：2026-09-Lab Session**

这一章材料里主要提到 Simplex Method 和 LP solver 的使用。

需要掌握的知识点：

1. **LP 最优解的四种情况**
   课件列出了四类情况：
   - 单一最优解；
   - 多个最优解；
   - 无可行解；
   - 无界。
2. **Simplex Method 单纯形法**
   要知道它是经典 LP 求解方法，由 Dantzig 提出。考试一般不一定要求完整手算复杂 simplex，但要理解它是在可行域顶点之间移动，寻找更优顶点。
3. **为什么 LP 求解器很重要**
   课件总结了 LP 的优势：精确优化、软件包多、速度快、变量数量可以很大，而且通常不需要像启发式算法那样调很多参数。
4. **LP Solver 使用能力**
   实验要求选择三个不同算法或不同语言的 LP solver，求解给定问题。也就是说要会用工具求解 LP，并比较不同 solver 的结果。
5. **LP relaxation 线性松弛**
   在整数问题中，把 $x_i\in{0,1} $放宽成 $0\le x_i\le 1)，就得到 LP relaxation。它可以很快求解，但结果可能不是整数，需要再转成可行整数解。

------

## 第8章 Integer linear programming algorithms

**整数线性规划算法**
**对应课件：2026-09-LP and ILP for Students；实验：2026-09-Lab Session**

这一章重点是理解 LP 和 ILP 的区别，以及为什么 ILP 比 LP 难。

需要掌握的知识点：

1. **ILP 的基本形式**
   ILP 与 LP 类似，但部分或全部变量必须是整数。例如背包问题中：
   $$
   x_i\in{0,1}
   $$
   这就是典型的 0-1 整数规划。
2. **LP 与 ILP 的核心区别**
   LP 的可行域是连续的，求解较快；ILP 的变量受到整数约束，可行解是离散的，通常更难。
3. **ILP Solver 的作用**
   可以直接求整数最优解，但计算时间可能随问题规模快速增加。
4. **LP Relaxation 与构造可行整数解**
   实验中要求用 LP solver 解 LP relaxation，再从 LP 解构造可行解；这说明 LP relaxation 可以作为一种近似或辅助方法。
5. **实验比较四类方法**
   实验要求在 100-item、200-item、400-item knapsack 上比较：
   - 生成 SA 初始解的启发式方法；
   - 自己设置参数的 SA；
   - LP relaxation 后构造可行解；
   - ILP solver。
     比较指标是 objective function value 和 total computation time。
6. **问题规模影响**
   要理解：随着物品数量从100增加到200、400，启发式方法、SA、LP relaxation、ILP solver 的计算时间增长方式不同。ILP 通常更精确，但大规模时可能更慢。

这一章复习重点是：**LP 快但可能给非整数解，ILP 精确但可能计算更慢，LP relaxation 可作为整数问题的辅助方法。**

------

## 这部分的复习优先级

**第一优先级：局部搜索与邻域结构**
要会解释 LS、neighborhood、first move、best move、local optimum、inversion。

**第二优先级：SA 和 TS**
重点比较二者如何跳出局部最优：SA 靠温度和概率，TS 靠 tabu list 和记忆机制。

**第三优先级：EA/GA**
掌握 population、selection、mutation、crossover、tournament selection、generation update。

**第四优先级：子集选择与背包问题**
会写 0-1 背包模型，会解释 greedy、local improvement、branch and bound、搜索空间为什么大。

**第五优先级：LP/ILP**
会建模，会区分 LP 和 ILP，会解释 LP relaxation、solver、单纯形法、无可行解、无界、多解等情况。

## 第9章 无约束非线性优化与梯度下降

**对应课件：2026-10-For-Students；实验：2026-10-Lab Session**

这一章重点是掌握无约束非线性优化问题的基本形式，即最小化非线性函数 $f(x )$，理解一维函数图像和二维等高线图在优化中的意义。课件从“Unconstrained nonlinear optimization Problem”开始，引出梯度下降的思想。

需要掌握的知识点：

1. **无约束非线性优化问题的表达**
   要会写出问题形式：
   $$
   \min f(x),\quad x\in R^n
   $$
   并理解 $x $是决策变量，$f(x) $是目标函数。
2. **梯度 / 导数的方向意义**
   一维情况下，若当前位置导数大于0，说明继续增大 $x $会使函数值上升，因此要向左移动；若导数小于0，则要向右移动。重点是理解“负梯度方向是下降方向”。
3. **梯度下降更新公式**
   要熟悉：
   $$
   x^{(k+1)}=x^{(k)}-\alpha \nabla f(x^{(k)})
   $$
   其中 $\alpha $是步长。要知道步长太大可能震荡或发散，步长太小收敛很慢。
4. **Constant Step Size 固定步长**
   要会解释固定步长梯度下降的搜索轨迹，理解为什么不同初始点、不同 $\alpha $会产生不同结果。
5. **Steepest Descent 最速下降法**
   要理解它和普通固定步长梯度下降的区别：最速下降通常要在线搜索中确定当前方向上的最佳步长。
6. **实验要会做的内容**
   实验要求你在二维函数上选择初始点和步长，展示梯度下降的移动序列，并比较不同步长的搜索效果；第二个函数是 Rosenbrock 类函数，重点观察狭长谷底中梯度下降容易慢、容易震荡的问题。

这一章复习时最重要的是：**会画搜索路径、会解释步长影响、会判断梯度下降是否收敛稳定。**

------

## 第10章 Newton 方法、线搜索与一维搜索

**对应课件：2026-11-for-Students；部分实验：2026-12-Lab Session**

这一章材料里主要讲了最优性条件、神经网络中的梯度下降、动量项、正则化，以及一维搜索方法，包括 Golden Section Search、Newton’s Method、Secant Method、Chord Method 和多维优化中的 Line Search。

需要掌握的知识点：

1. **最优性条件的直观理解**
   无约束问题中，局部最优点通常满足：
   $$
   \nabla f(x)=0
   $$
   课件也用图示区分了无约束、有等式约束、有不等式约束时最优点可能出现的位置。
2. **神经网络学习与梯度下降的关系**
   神经网络训练可以看成最小化误差函数 $E(w )$，通过调整权重 $w $来降低误差。课件中把神经网络学习公式和梯度下降公式对应起来。
3. **Momentum 动量项**
   要理解动量项的作用：
   - 正面效果：加速沿稳定方向的收敛，减少“来回小步走”；
   - 负面效果：可能因惯性过大而越过最优点、产生震荡。
     实验要求你比较加入动量项前后的正负效果。
4. **Regularization 正则化**
   要理解：
   $$
   E(w)\rightarrow E(w)+\lambda|w|^2
   $$
   它的作用是控制模型复杂度，避免过拟合。还要知道 $\lambda $太小约束弱，太大可能欠拟合。
5. **一维搜索问题**
   课后实验假设函数形式未知，只能计算 $f(x )$，且最优解在 $[0,1] $内、函数单峰。你需要思考在只能检查2个、3个、20个点时，如何安排采样点以尽量缩小包含最优解的区间。
6. **Golden Section Search 黄金分割搜索**
   要掌握其目的：在单峰区间内用较少函数评价逐步缩小搜索区间。
7. **Newton’s Method 牛顿法**
   要理解牛顿法利用二阶信息或局部二次近似寻找极值。实验还要求你构造一个在某些初始点上 Newton 方法效果不好的函数，因此要知道牛顿法可能受初始点、曲率、非凸性影响。
8. **Line Search 多维线搜索**
   多维优化中，更新形式为：
   $$
   x^{(k+1)}=x^{(k)}+\alpha_k d^{(k)}
   $$
   重点是确定搜索方向 $d^{(k)} $和步长 $\alpha_k$，并把多维问题转化为沿某一方向的一维搜索。

注意：课程目录里写了 **Levenberg-Marquardt modification**，但目前这批上传材料中没有看到对 LM 方法的完整展开。因此如果老师后续补充，需要重点看它如何在 Newton 方法和梯度下降之间折中。

------

## 第11章 Quasi-Newton 方法与共轭方向法

**当前上传材料中没有看到完整独立课件**

课程大纲中有这一章：**Quasi-Newton methods and conjugate direction methods**，但这批文件里没有看到完整讲解内容，只能从第10章的线搜索部分衔接过去。

如果这章考试覆盖，建议至少掌握：

1. **Quasi-Newton 的基本思想**
   不直接计算 Hessian 矩阵，而是用迭代信息近似 Hessian 或 Hessian 逆矩阵。
2. **为什么需要 Quasi-Newton**
   Newton 方法收敛快，但二阶导数计算成本高；Quasi-Newton 用近似方法降低计算量。
3. **搜索方向与线搜索的关系**
   Quasi-Newton 和共轭方向法通常都要结合线搜索确定步长。
4. **共轭方向法的核心**
   搜索方向之间不是简单正交，而是相对于某个矩阵共轭，从而避免重复搜索。

这一章目前建议作为“概念预习”，等老师补完整课件后再细化公式。

------

## 第12章 等式约束非线性优化

**当前上传材料中只出现了最优性条件示意，没有完整章节内容**

课件中只用图示展示了有等式约束时，最优点不一定满足普通的 $\nabla f(x)=0)，而是受到可行曲线或可行面的限制。

最低需要掌握：

1. **等式约束问题形式**
   $$
   \min f(x),\quad h(x)=0
   $$
2. **可行域 / 可行曲线的含义**
   解必须落在约束条件允许的集合上。
3. **约束最优和无约束最优的区别**
   无约束最优点看整个空间；等式约束最优点只看约束曲线或约束面上的最优。
4. **Lagrange 乘子法的基本思想**
   如果后续老师讲，要重点掌握：
   $$
   \nabla f(x)+\lambda \nabla h(x)=0
   $$

------

## 第13章 不等式约束非线性优化

**当前上传材料中也只出现了可行域和边界最优的图示**

课件中用图说明了不等式约束下的可行域，最优点可能在区域内部，也可能在边界上。

最低需要掌握：

1. **不等式约束问题形式**
   $$
   \min f(x),\quad g_i(x)\le 0
   $$
2. **Feasible Region 可行域**
   所有满足约束的点构成可行域，优化只能在可行域内进行。
3. **Active Constraint 活跃约束**
   如果最优点落在边界上，对应约束通常是活跃的。
4. **KKT 条件的基本结构**
   如果考试讲到，需要掌握：可行性、梯度平衡、互补松弛、乘子非负性。

------

## 第14章 多目标优化基本概念

**对应课件：2026-12-Multi-Objective Basic Concepts；实验：2026-12-Lab Session**

这一章是后面 EMO 的基础。课件从正则化引出多目标思想：最小化 $E(w)+\lambda|w|^2 $可以看作在误差 $E(w) $和复杂度 $|w|^2 $之间做权衡。

需要掌握的知识点：

1. **单目标、多目标、Many-objective 的区别**
   单目标只有一个 $f(x )$，多目标有多个 $f_1(x),f_2(x),...,f_m(x )$。目标数很多时称为 many-objective optimization。
2. **目标冲突 Conflict**
   多目标优化的关键是目标之间往往不能同时达到最好，比如价格低和质量高可能冲突。
3. **Pareto Dominance 帕累托支配**
   解 A 支配解 B，意思是 A 在所有目标上不差于 B，并且至少一个目标更好。
4. **Pareto Optimal Solution 帕累托最优解**
   如果没有其他解能支配它，它就是 Pareto optimal solution。
5. **Pareto Front 与 Pareto Set**
   决策空间中的 Pareto 最优解集合是 Pareto set；目标空间中的对应曲线或曲面是 Pareto front。
6. **Non-dominated Solution Set 非支配解集**
   在有限个候选解中，没有被其他候选解支配的解组成非支配解集。
7. **多目标优化的最终目标**
   不是只找一个解，而是找到一组能代表 Pareto front 的解，然后再由决策者选择。
8. **实验要会做的内容**
   实验要求计算随机点之间的支配概率，以及随机生成多个点时非支配解的期望数量。要理解：目标维度越高，随机解之间越不容易互相支配，因此非支配解比例会变高。

------

## 第15章 多目标优化中搜索单个最终解

**对应课件：2026-12-Multi-Objective Basic Concepts 后半部分**

这一章重点是：如何在多目标问题中利用决策者偏好，最后得到一个单一解。课件把方法分成两类：优化前使用额外信息，或者优化后再由决策者选择。

需要掌握的知识点：

1. **Traditional Approach 传统方法**
   在优化之前先把多个目标合成为一个目标函数，例如加权和：
   $$
   f(x)=w_1f_1(x)+w_2f_2(x)
   $$
   然后求这个单目标问题的最优解。
2. **Weighted Sum 加权和方法**
   要会解释权重 $w_1,w_2 $的意义：权重体现决策者偏好。
3. **加权和方法的局限**
   不是所有 Pareto 最优点都一定能通过线性加权和找到，尤其是在非凸 Pareto front 上。
4. **Target Solution / Reference Point 思想**
   决策者可以先给出理想目标或参考方向，算法再寻找最接近偏好的解。
5. **EMO Approach 与传统方法区别**
   EMO 先找一批 Pareto 解，再让决策者选择；传统方法先给偏好，再优化出一个解。

这一章考试很可能会问：**“多目标问题如何转化为单目标问题？”“为什么加权和方法有局限？”**

------

## 第16章 多目标优化中搜索多个解：EMO 算法

**对应课件：2026-13-EMO Students；实验：2026-13-Lab Session**

这一章是重点。课件明确说 EMO 算法设计目标是：在整个 Pareto front 上找到一组分布良好的解。

需要掌握的知识点：

1. **EMO 的基本目标**
   同时追求两个方面：
   - Convergence：解要接近 Pareto front；
   - Diversity：解要在 Pareto front 上分布均匀。
2. **Evolutionary Computation 基本流程**
   种群初始化、评价个体、选择好个体、生成新个体，反复迭代。课件强调每个个体在多目标情况下要用多个目标进行评价。
3. **Solution-level Evaluation 与 Solution-set-level Evaluation**
   一个是算法内部评价单个解的 fitness；另一个是比较整个算法最终得到的解集 performance。
4. **Pareto dominance-based algorithms**
   要知道 MOGA、NPGA、NSGA、NSGA-II 这类算法主要依赖 Pareto 支配关系进行选择。
5. **NSGA-II**
   重点掌握：
   - non-dominated sorting 非支配排序；
   - crowding distance 拥挤距离；
   - elitism 精英保留；
   - 为什么它在两目标问题上较有效。
6. **NSGA-II 的困难**
   在多目标尤其 many-objective 问题中，很多解都互不支配，Pareto dominance 的选择压力下降；crowding distance 是按目标轴投影计算，在三目标及以上时可能导致分布不均。课后实验也专门要求修改 NSGA-II 的选择机制来获得更均匀分布。
7. **MOEA/D**
   要掌握 decomposition 思想：把一个多目标问题分解成多个标量子问题。重点包括 weighted sum、Tchebycheff、PBI、weight vector、local comparison / replacement。
8. **Indicator-based algorithms / SMS-EMOA**
   要知道这类算法用性能指标指导选择，例如基于 hypervolume contribution 删除贡献最小的解。
9. **Many-objective optimization**
   要理解目标数增加后的困难：可视化困难、非支配解比例上升、HV 计算量大、参考点或权重向量设计困难。
10. **实验要会做的内容**
    给定14个网格点，用 NSGA-II 选择7个下一代解；再用自己的想法选择更均匀的解；最后尝试修改 NSGA-II 的 generation update 或 crowding distance，使三目标及以上问题也能得到更均匀的解集。

------

## 第16章补充：EMO 性能指标与解集评价

**对应课件：2026-14-EMO Indicators；实验：2026-14-Indicators Lab Session**

这部分虽然文件名是第14次课，但内容上属于 EMO 后续：如何评价一个算法得到的解集。课件开头强调 crowding distance 计算时需要对每个目标做归一化。

需要掌握的知识点：

1. **单目标优化与多目标优化评价差异**
   单目标优化最终是一个解，比较容易；EMO 最终是一组解，比较的是 solution set / population performance。
2. **Performance Indicator 的作用**
   用一个数值评价一个解集的质量，通常考察收敛性、分布范围、均匀性或综合表现。
3. **Convergence 指标**
   例如 GD，用来衡量解集距离 Pareto front 有多近。
4. **Diversity 指标**
   包括 spread、maximum spread、spacing、Deb’s spread 等，用来评价解集覆盖范围和均匀性。
5. **IGD / IGD+**
   IGD 衡量 Pareto front 上参考点到最近解的平均距离。要知道它依赖 reference set，而且 IGD 不一定 Pareto compliant。
6. **Epsilon Indicator**
   衡量一个解集需要平移多少才能弱支配另一个解集。
7. **Hypervolume, HV**
   重点掌握：HV 是解集相对于 reference point 所支配区域的体积或面积；reference point 的选择会明显影响结果。
8. **Pareto Compliance**
   要理解一个指标是否与 Pareto 支配关系一致。HV 通常是重点指标。
9. **可视化评价**
   两目标问题可以用 attainment surface；many-objective 问题可用 parallel coordinates，但四个及以上目标的可视化会变难。
10. **公平比较问题**
    不同算法的种群规模会影响评价结果，因此公平比较时最好从所有已搜索解中选择相同数量的解再比较。
11. **实验要会做的内容**
    实验给出：
    $$
    f_1(x)=x_1,\quad f_2(x)=x_2,\quad x_1+x_2\le 1
    $$
    Pareto front 是从 $(0,1) $到 $(1,0) $的线段。你需要在不同 reference point 下找使 HV 最大的单解、两个解、五个解，并在参考点均匀分布时找使 IGD 最小的五个解。

------

## 复习优先级

最应该先掌握的是：

**第一层：基本公式和概念**
梯度下降、步长、线搜索、Newton 方法、Pareto dominance、Pareto optimal、Pareto front、non-dominated set。

**第二层：算法机制**
NSGA-II、crowding distance、MOEA/D、SMS-EMOA、HV-based selection。

**第三层：实验题能力**
会画梯度下降路径，会比较不同步长；会判断支配关系；会用 NSGA-II 选下一代；会根据 HV / IGD 解释为什么某组解更好。

**第四层：容易出问答题的点**
为什么梯度下降步长不能随便选；为什么 Newton 方法可能失败；为什么多目标优化不能简单说“哪个解最好”；为什么 many-objective 问题比两目标更难；为什么 HV 依赖 reference point。



## 到这里整门课的大致章节逻辑

整门课可以这样串起来：

**第1章**：告诉你什么是优化问题。
**第2章**：先学最简单的构造型启发式算法——贪心。
**第3章**：发现贪心不够好，于是用局部搜索改进。
**第4章**：发现局部搜索会陷入局部最优，于是引入 VNS、SA、TS、EA。
**第5章**：把这些思想用于子集选择、背包等组合优化问题。
**第6—8章**：进入 LP / ILP，用数学规划和 solver 处理线性优化。
**第9—13章**：进入非线性优化，学习梯度下降、Newton、约束优化。
**第14—16章**：进入多目标优化，学习 Pareto、EMO、NSGA-II、MOEA/D、HV、IGD 等。