下面我按你的 3 个要求来讲。先说明：我把课件内容按“知识框架”整理，不是逐页翻译 190 页，而是把 EMO/NSGA-II 相关的核心概念、算法、性质和课件想强调的问题串起来。

------

# 1. 用中文讲解我刚刚的解答

题目是一个**两目标最大化问题**，目标是从 14 个点中选出 7 个作为下一代种群。课件中的 Lab Session 明确要求：Task 1 用 NSGA-II 选 7 个点，Task 2 用自己的想法选一个更好的 7 点集合，Task 3 修改 NSGA-II 的 generation update，Task 4 进一步考虑三目标及更多目标的情况。

14 个点坐标是：

| 点   | 坐标    |
| ---- | ------- |
| 0    | (1,18)  |
| 1    | (3,18)  |
| 2    | (3,16)  |
| 3    | (4,17)  |
| 4    | (5,15)  |
| 5    | (6,14)  |
| 6    | (8,13)  |
| 7    | (9,12)  |
| 8    | (10,10) |
| 9    | (12,8)  |
| A    | (13,6)  |
| B    | (15,3)  |
| C    | (17,1)  |
| D    | (18,0)  |

## Task 1：用 NSGA-II 选择 7 个解

因为是**最大化**，一个点如果在两个目标上都不差，而且至少一个目标更好，就支配另一个点。

点 0 = (1,18) 被点 1 = (3,18) 支配，因为点 1 的横坐标更大，纵坐标一样。

点 2 = (3,16) 被点 1 = (3,18) 支配，也被点 3 = (4,17) 支配。

所以第一非支配层是：

[
F_1={1,3,4,5,6,7,8,9,A,B,C,D}
]

这个 front 里有 12 个点，但我们只需要选 7 个。NSGA-II 的规则是：先按非支配排序，front 越靠前越好；如果同一层点太多，就用 **crowding distance，拥挤距离** 来选。课件中也强调 NSGA-II 的主要评价准则是 non-dominated sorting，次要准则是 crowding distance。

拥挤距离大的点优先保留，因为它们所在区域比较稀疏。

计算后，拥挤距离大致是：

| 点   | 拥挤距离 |
| ---- | -------- |
| 1    | ∞        |
| 3    | 0.300    |
| 4    | 0.300    |
| 5    | 0.311    |
| 6    | 0.311    |
| 7    | 0.300    |
| 8    | 0.422    |
| 9    | 0.422    |
| A    | 0.478    |
| B    | 0.544    |
| C    | 0.367    |
| D    | ∞        |

所以 NSGA-II 会选拥挤距离最大的 7 个：

[
\boxed{{1,8,9,A,B,C,D}}
]

也就是：

[
\boxed{(3,18),(10,10),(12,8),(13,6),(15,3),(17,1),(18,0)}
]

这个结果的缺点是：选出来的点偏向右下区域，中间和左上区域覆盖得不好。所以它虽然符合 NSGA-II 规则，但分布并不均匀。

------

## Task 2：用“好的 EMO 算法”的思想选择 7 个解

EMO 算法的目标不是只找到一个最优解，而是找到一组**接近 Pareto front 且分布均匀**的解。课件第 2–3 页就强调，EMO 算法设计目标是找到一组 well-distributed solutions over the entire Pareto front。

所以我自己的选择原则是：

保留两个端点，然后沿 Pareto front 尽量均匀取点。

我选的是：

[
\boxed{{1,4,6,8,A,B,D}}
]

坐标是：

[
\boxed{(3,18),(5,15),(8,13),(10,10),(13,6),(15,3),(18,0)}
]

这个集合比 Task 1 的结果更均匀，因为它覆盖了左上、中间和右下区域。

------

## Task 3：修改 NSGA-II 的 generation update

原始 NSGA-II 的问题是：crowding distance 只计算一次。选或删掉一些点之后，剩下点之间的拥挤关系已经变了，但 NSGA-II 不重新计算。

所以我提出的修改是：

**反复重新计算 crowding distance。**

具体做法：

1. 先做非支配排序。
2. 如果最后一个 front 中点太多，就计算 crowding distance。
3. 删除拥挤距离最小的点。
4. 删除后重新计算 crowding distance。
5. 重复这个过程，直到只剩下需要的数量。

在这个例子中，可以依次删除：

[
3 \rightarrow 7 \rightarrow 5 \rightarrow C \rightarrow 9
]

最后留下：

[
\boxed{{1,4,6,8,A,B,D}}
]

这正好和 Task 2 中“更均匀”的选择一致。

课件中也给出了类似补充方向：NSGA-II 的 ((\mu+\mu))-style framework 可以通过 recalculation 或 ((\mu+1))-style 来修改。

------

## Task 4：三目标或更多目标时怎么改

即使用了 crowding distance recalculation，三目标问题中也不能保证均匀。原因是 NSGA-II 的 crowding distance 是在每一个目标轴上分别计算的，本质上是 projection-based，也就是投影式距离。课件 Task 4 明确说：三目标中即使重新计算 crowding distance 也不能得到均匀解集，因为 crowding distance 是在 objective space 的每个坐标轴上计算的。

因此，我建议把 crowding distance 换成真正的多维空间密度度量。

一种简单方法是：

先对每个目标归一化：

[
z_m(i)=\frac{f_m(i)-f_m^{min}}{f_m^{max}-f_m^{min}}
]

然后计算点与点之间的欧氏距离。对每个解，计算它到 (k) 个最近邻的平均距离：

[
D(i)=\frac{1}{k}\sum_{j \in kNN(i)} ||z(i)-z(j)||
]

(D(i)) 越小，说明这个点附近越拥挤，就越应该删除。这样比原始 crowding distance 更适合三目标或更多目标，因为它考虑的是整个多维 objective space 的几何距离，而不是单独看每个坐标轴。

更强的方法是使用 **reference directions / reference vectors**，类似 NSGA-III 或 MOEA/D 的思想：

1. 生成均匀分布的参考方向。
2. 把每个解分配到最近的参考方向。
3. 优先选择解较少的方向。
4. 同一方向内选择收敛性更好的解。

这样可以更好地保持三维或高维 Pareto front 上的均匀分布。

------

# 2. 参考课件，我还需要补充什么

我刚才的解答主要解决了 Lab 的 4 个任务，但参考课件，还可以补充以下几点。

第一，课件反复强调 EMO 的两个目标：**convergence 收敛性**和 **diversity 多样性**。收敛性是让种群靠近 Pareto front，多样性是让解均匀覆盖整个 Pareto front。算法设计的核心问题就是平衡这两者。

第二，Task 1 的现象不是偶然的，而是 NSGA-II 的结构性问题。课件总结 NSGA-II 的困难包括：((\mu+\mu))-style framework、projection-based crowding distance calculation、Pareto dominance-based main fitness criterion。尤其在三目标和更多目标中，这些问题会明显放大。

第三，课件中给出的改进方向不只 crowding distance recalculation，还包括 ((\mu+1))-style。也就是说，不一定一次从 (2\mu) 个解中选 (\mu) 个，可以每次加入一个新解、删除一个最差解，并在每一步更新密度信息。

第四，三目标以上的问题应该参考 MOEA/D、NSGA-III、SMS-EMOA 等算法。MOEA/D 通过 decomposition 把多目标问题分解成多个单目标子问题，SMS-EMOA 直接优化 hypervolume 指标，NSGA-III 使用 reference points/reference directions 来处理 many-objective optimization。课件也提到，MOEA/D 使用 weighted sum、Tchebycheff、PBI 等 scalarizing functions。

第五，评价一个 EMO 算法时不能只看“选出来的点好不好看”。课件区分了两个层次：solution-level evaluation 是算法内部评价单个解，solution set-level evaluation 是评价整个解集，也就是 performance。 一个算法可能在 HV 指标上好，但在 IGD 或均匀性上不好；课件中也举例说明 SMS-EMOA 和 MOEA/D 在 DTLZ2 上，HV-based comparison 和 IGD-based comparison 可能给出不同结论。

------

# 3. 课件知识点总讲解：EMO、NSGA-II、概念、性质和算法

## 3.1 什么是多目标优化

单目标优化只有一个目标，例如：

[
\max f(x)
]

多目标优化有多个目标，例如：

[
\max f_1(x), f_2(x), \dots, f_m(x)
]

在多目标优化中，通常不存在一个解能同时让所有目标都达到最好。比如买车时，价格低、性能高、油耗低、空间大，这些目标往往冲突。

所以多目标优化的目标不是找一个唯一最优解，而是找一组折中解。

------

## 3.2 Pareto dominance，Pareto 支配

以最大化为例，解 (x) 支配解 (y)，记作：

[
x \prec y
]

当且仅当：

1. 对所有目标 (i)，都有
   [
   f_i(x)\ge f_i(y)
   ]
2. 至少存在一个目标 (j)，使得
   [
   f_j(x)>f_j(y)
   ]

也就是说，(x) 在所有目标上都不比 (y) 差，并且至少一个目标更好。

被其他解支配的解叫 dominated solution；不被任何其他解支配的解叫 nondominated solution。

------

## 3.3 Pareto optimal solution, Pareto set, Pareto front

**Pareto optimal solution**：在整个可行域中不被任何其他解支配的解。

**Pareto set**：所有 Pareto optimal solutions 在决策空间中的集合。

**Pareto front**：这些 Pareto optimal solutions 映射到目标空间后的集合。

简单说：

决策空间中叫 Pareto set，目标空间中叫 Pareto front。

------

## 3.4 Pareto dominance 的性质

在最大化问题中，严格 Pareto dominance 有几个重要性质：

**非自反性**：一个解不会严格支配自己。

**非对称性**：如果 (x) 支配 (y)，那么 (y) 不可能支配 (x)。

**传递性**：如果 (x) 支配 (y)，(y) 支配 (z)，那么 (x) 支配 (z)。

这些性质让我们可以用 dominance 来给解排序。

但是它也有缺点：目标数越多，两个随机解之间越不容易互相支配。所以 many-objective problems 中，很多解都会变成 nondominated solutions，导致选择压力下降。

------

## 3.5 EMO 是什么

EMO 是 Evolutionary Multi-Objective Optimization，多目标进化优化。

它把进化算法用于多目标优化。

普通进化算法的流程是：

1. 初始化种群。
2. 评价个体。
3. 好个体生存。
4. 用好个体产生新个体。
5. 重复迭代。

多目标进化算法的区别是：每个个体不是用一个目标评价，而是用多个目标评价。课件中明确指出，multi-objective evolutionary algorithms 与 single-objective optimization 的区别就在于每个个体要用 (m) 个目标来评价。

------

## 3.6 EMO 的两个核心目标

课件强调两个 sub-goals：

**Convergence 收敛性**：让种群尽量靠近 Pareto front。

**Diversity 多样性**：让种群在整个 Pareto front 上均匀分布。

这两个目标经常冲突。只追求收敛，解会集中到某一小段；只追求多样性，解可能离 Pareto front 很远。

EMO 算法设计的核心就是平衡 convergence 和 diversity。

------

## 3.7 Fitness 和 Performance 的区别

课件中有一个很重要的区分：

**Fitness：solution level evaluation**

这是算法内部评价单个解的方式。比如 NSGA-II 里，单个解的 fitness 由 nondominated rank 和 crowding distance 决定。

**Performance：solution set level evaluation**

这是评价整个算法输出结果的方式。比如看最后得到的解集是否接近 Pareto front，是否分布均匀，HV 或 IGD 是否好。

所以，一个解在算法内部 fitness 高，不代表整个解集 performance 一定好。

------

## 3.8 Pareto dominance-based EMO 的基本思想

早期 EMO 算法主要靠两个机制：

**Pareto dominance**：推动种群靠近 Pareto front。

**Crowding**：保持种群多样性。

课件第 17–24 页反复讲这两个思想：Pareto dominance 用来提高 convergence，crowding 用来维护 diversity。

------

## 3.9 非精英 EMO 和精英 EMO

早期 1990s 的算法，如 MOGA、NPGA、NSGA，是 non-elitist algorithms。它们的特点是：

1. 非精英机制。
2. 用 Pareto dominance 评价 fitness。
3. 有多样性维护机制。

缺点是 convergence 较弱。

后来 ZDT 等测试问题出现后，人们发现随机初始解通常离 Pareto front 很远，因此需要更强的 convergence ability。于是 late 1990s 和 2000s 出现了 elitist EMO algorithms，例如 SPEA、NSGA-II、MOEA/D。课件也把这几个算法列为高引用代表算法。

------

## 3.10 NSGA-II 的算法框架

NSGA-II 是一个经典的 elitist EMO algorithm。

它使用 ((\mu+\mu))-style framework：

当前种群大小是 (\mu)。

生成 offspring population，大小也是 (\mu)。

把父代和子代合并，得到 (2\mu) 个解。

从这 (2\mu) 个解中选出最好的 (\mu) 个作为下一代。

选择标准是：

1. 主标准：non-dominated sorting。
2. 次标准：crowding distance。

课件第 49–53 页就是 NSGA-II 的基本框架、fitness evaluation 和 generation update。

------

## 3.11 Non-dominated sorting，非支配排序

NSGA-II 会把所有解分成多个 front：

第一层 (F_1)：所有 nondominated solutions。

第二层 (F_2)：去掉 (F_1) 后，剩余解中的 nondominated solutions。

第三层 (F_3)：继续重复。

front 越靠前，rank 越小，fitness 越高。

也就是说：

[
F_1 \succ F_2 \succ F_3 \succ \dots
]

------

## 3.12 Crowding distance，拥挤距离

在同一个 front 内，NSGA-II 需要判断哪些解更值得保留。这时用 crowding distance。

基本思想是：

如果一个解周围很空，它的 crowding distance 大，应该保留。

如果一个解周围很挤，它的 crowding distance 小，可以删除。

对于每个目标，先按该目标值排序。边界点给无穷大，因为要保留两端 extreme solutions。中间点的距离由左右邻居的目标值差决定。

公式可以理解为：

[
CD(i)=\sum_{k=1}^{m}
\frac{f_k(i+1)-f_k(i-1)}
{f_k^{max}-f_k^{min}}
]

这里的 (k) 是目标编号。

------

## 3.13 NSGA-II 的 parent selection

NSGA-II 通常用 binary tournament selection。

两个个体比赛：

1. rank 小的赢。
2. 如果 rank 一样，crowding distance 大的赢。

这体现了 NSGA-II 的两个偏好：

先要收敛性，再要多样性。

------

## 3.14 NSGA-II 的主要问题

课件总结 NSGA-II 有三个困难：

1. ((\mu+\mu))-style framework。
2. Projection-based crowding distance calculation。
3. Pareto dominance-based main fitness criterion。

第一个问题是，一次性从 (2\mu) 个解中选 (\mu) 个，选完后不再根据新的局部密度更新。

第二个问题是 crowding distance 是按每个目标轴分别计算的。二维时通常还可以，但三维或更高维时会出问题。

第三个问题是多目标数量增加后，很多解都互不支配，Pareto dominance 的选择压力变弱。

------

## 3.15 Dominance resistant solutions

课件提到 dominance resistant solutions，简称 DRSs。

这类解在某些目标上特别好，但在其他目标上特别差。

它们可能离真正的 Pareto front 很远，但是因为它们某些目标值极端好，所以不容易被其他解支配。

这会导致 NSGA-II 在 many-objective problems 中保留一些并不真正好的解。

------

## 3.16 为什么二维和三维差别很大

二维问题中，Pareto front 通常是一条曲线。crowding distance 沿两个坐标轴计算，基本能反映曲线上点与点之间的疏密程度。

三目标问题中，Pareto front 通常是一个曲面。点之间的真实邻近关系是三维几何关系，而不是某个单独坐标轴上的距离。

课件明确指出：projection-based crowding distance 对二维可以，但对 3-D problematic。

所以 Task 4 要求我们修改 crowding distance 或创造新机制。

------

## 3.17 MOEA/D 的思想

MOEA/D 是 Multi-Objective Evolutionary Algorithm based on Decomposition。

它的核心思想是：

把一个多目标问题分解成很多个单目标子问题。

每个子问题对应一个 weight vector。

比如两目标问题中，不同权重代表 Pareto front 上不同方向。

MOEA/D 使用 scalarizing functions 把多个目标合成一个标量目标。课件中列出三种典型函数：

1. Weighted Sum。
2. Weighted Tchebycheff。
3. PBI，Penalty-based Boundary Intersection。

------

## 3.18 Weighted Sum 的性质

Weighted Sum 把目标加权求和：

[
g^{WS}(x)=\sum_{i=1}^{m} w_i f_i(x)
]

优点是简单。

缺点是：对非凸 Pareto front 不好，可能找不到某些 Pareto optimal solutions。

------

## 3.19 Tchebycheff 的性质

Weighted Tchebycheff 通常写成：

[
g^{TE}(x)=\max_i {w_i |z_i^*-f_i(x)|}
]

其中 (z^*) 是 ideal point。

重要性质：课件指出，Tchebycheff function 可以得到任意 Pareto solution。

因此它比 weighted sum 更适合非凸 Pareto front。

------

## 3.20 PBI 的思想

PBI 全称 Penalty-based Boundary Intersection。

它把评价分成两部分：

1. 沿 reference direction 的距离，表示 convergence。
2. 偏离 reference direction 的距离，表示 diversity。

一般形式是：

[
g^{PBI}=d_1+\theta d_2
]

其中 (d_1) 衡量沿方向的进展，(d_2) 衡量偏离方向的程度，(\theta) 是惩罚参数。

PBI 常用于 MOEA/D 和 reference-vector-based algorithms。

------

## 3.21 MOEA/D 的机制

MOEA/D 有两个重要机制：

**Local selection**

相近 weight vectors 对应的子问题互为邻居。交叉变异时，优先从邻居中选父代。

**Local comparison / multiple replacement**

一个新 offspring 生成后，会和邻居子问题中的解比较。如果新解对多个邻居子问题更好，就可以替换多个邻居。

------

## 3.22 MOEA/D 的困难

课件列出 MOEA/D 的困难：

1. 一个新解可能比所有邻居都好。
2. 一个新解可能离它的 neighborhood 很远。
3. 均匀 weight vectors 不一定合适。
4. many-objective problems 中没有足够的 inside weight vectors。

这说明 reference vectors/weight vectors 的设计非常重要。

------

## 3.23 SMS-EMOA 的思想

SMS-EMOA 是 indicator-based EMO algorithm，通常基于 hypervolume。

它的基本思想是：

既然 EMO 算法最终要用 performance indicator 来评价，不如直接优化这个 indicator。课件也这样解释 indicator-based EMO 的动机。

SMS-EMOA 使用 ((\mu+1)) update：

1. 当前有 (\mu) 个解。
2. 生成 1 个新解。
3. 从 (\mu+1) 个解中删除一个最差解。
4. 保持种群大小为 (\mu)。

通常删除 hypervolume contribution 最小的解。

------

## 3.24 Hypervolume, HV

Hypervolume 衡量一个解集支配的目标空间体积。

最大化问题中，给定 reference point，解集越靠近 Pareto front 且覆盖越广，HV 通常越大。

HV 的优点是同时考虑 convergence 和 diversity。

缺点是：

1. 计算量大，尤其是高维。
2. reference point 选择困难。
3. HV 最优的分布不一定看起来最均匀。

课件也列出 SMS-EMOA 的三大困难：uniformity 不一定好，HVC 计算量大，reference point specification 困难。

------

## 3.25 IGD, GD, Spacing 等指标

虽然课件重点更多放在 HV、IGD 对比上，但 EMO 常见 performance indicators 包括：

**GD，Generational Distance**

衡量得到的解集离 Pareto front 有多近，偏重 convergence。

**IGD，Inverted Generational Distance**

衡量 Pareto front 上参考点到得到的解集的距离，兼顾 convergence 和 diversity。

**Spacing**

衡量解之间距离是否均匀。

**Maximum Spread**

衡量解集覆盖范围。

课件中提到，同一个结果用 HV 和 IGD 评价可能得出不同结论，所以算法比较需要结合多个指标和 decision maker preference。

------

## 3.26 NSGA-III 和 many-objective optimization

Many-objective optimization 通常指目标数较多的问题。课件中把三目标仍作为 multi-objective problem，而四目标及以上开始讨论 many-objective problem 的困难。

NSGA-III 的核心思想是使用 reference points/reference directions。

它不是只靠 crowding distance，而是用参考方向来维持解集分布。

基本流程是：

1. 做 non-dominated sorting。
2. 如果最后一个 front 需要截断，就用 reference directions 做 niching。
3. 优先选择稀疏 reference direction 上的解。
4. 这样可以在高维 Pareto front 上保持更均匀分布。

课件中也提到，many-objective problems 中 MOEA/D 没有 inside weight vectors 的问题，可以用 NSGA-III 的 two-layer method 来修改。

------

## 3.27 测试问题和算法发展的关系

课件有一条很重要的历史线：

1990s：简单两目标问题，不需要很强收敛能力。MOGA、NPGA、NSGA 等 non-elitist algorithms 可以工作。

2000 左右：ZDT 问题出现，随机初始解离 Pareto front 很远，需要强收敛能力，因此 SPEA、SPEA2、NSGA-II 等 elitist algorithms 变重要。

2000s：DTLZ、WFG 等 scalable test problems 出现，可以任意指定目标数，MOEA/D 和 SMS-EMOA 开始流行。

2010s：many-objective optimization 成为重点，HypE、NSGA-III 等算法出现。

------

## 3.28 当前 EMO 热点

课件后面还总结了当前热点，包括：

**Many-objective optimization**

目标数很多，Pareto dominance 失效，visualization 困难。

**Large-scale multi-objective optimization**

决策变量很多，例如 1000 或 10000 维。

**Expensive multi-objective optimization**

每次评价很贵，需要 surrogate model，比如用近似模型预测目标值。

**Weight/reference vector adaptation**

固定 weight vectors 不一定适合复杂 Pareto front，需要自适应调整。

**Constrained multi-objective optimization**

有约束条件，需要考虑如何利用 infeasible solutions。

**Multi-modal multi-objective optimization**

同一个 Pareto front 点可能对应多个不同的 Pareto optimal solutions。

**External archive**

把历史上找到的好解存起来，并研究如何利用 archive 生成新解、选择下一代、选择最终输出。

**Preference incorporation**

把 decision maker 的偏好加入算法，不一定追求整个 Pareto front，而是重点搜索用户关心的区域。

**Pareto front modeling**

不只输出离散解，而是尝试建模整个 Pareto front，让决策者可以选择任意 front 上的点。

------

# 最后总结

这次 Lab 的核心不是单纯算出 7 个点，而是理解：

NSGA-II 的标准结果是：

[
\boxed{{1,8,9,A,B,C,D}}
]

但这个结果分布不均匀。

一个更好的 EMO 选择是：

[
\boxed{{1,4,6,8,A,B,D}}
]

Task 3 的关键思想是：**重新计算 crowding distance，或者改成 ((\mu+1))-style update。**

Task 4 的关键思想是：**三目标及以上不能只用按坐标轴投影的 crowding distance，需要用多维距离、kNN 密度、reference directions、NSGA-III 式 niching，或者 HV/IGD 等 indicator-based 机制。**