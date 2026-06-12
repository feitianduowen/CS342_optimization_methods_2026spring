import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 通用梯度下降算法
# ==========================================
def gradient_descent(grad_f, f, x0, alpha, iterations=50):
    x = np.array(x0, dtype=float)
    history = [x.copy()]
    
    for _ in range(iterations):
        grad = grad_f(x)
        x = x - alpha * grad
        history.append(x.copy())
        
        # 安全机制：防止数值溢出
        if np.any(np.abs(x) > 1e4):
            break
            
    return np.array(history)

# ==========================================
# Task 1: 二次函数优化
# ==========================================
def f1(x1, x2):
    return (x1 + 1)**2 / 9 + (x2 + 1)**2

def grad_f1(x):
    return np.array([2*(x[0] + 1)/9, 2*(x[1] + 1)])

x0_task1 = [3.0, 4.0]
alphas_task1 = [0.1, 0.5, 0.9, 1.05]
histories_task1 = []

print("="*60)
print(f"{'Task 1: Quadratic Function Optimization Results':^60}")
print("="*60)
print(f"{'Alpha':<8} | {'Iter':<5} | {'Final x1':<10} | {'Final x2':<10} | {'Final f(x)':<12}")
print("-" * 60)

for alpha in alphas_task1:
    history = gradient_descent(grad_f1, f1, x0_task1, alpha, iterations=40)
    histories_task1.append(history)
    
    final_x = history[-1]
    final_val = f1(final_x[0], final_x[1])
    print(f"{alpha:<8.2f} | {len(history)-1:<5} | {final_x[0]:<10.6f} | {final_x[1]:<10.6f} | {final_val:<12.6e}")

# 绘制 Task 1: x1 vs ln(|x2|)
plt.figure(figsize=(10, 6))
colors = ['red', 'cyan', 'magenta', 'orange']

for i, (history, alpha) in enumerate(zip(histories_task1, alphas_task1)):
    x1_vals = history[:, 0]
    # 使用 np.log 并且加上 1e-10 防止 log(0) 报错
    x2_ln_abs = np.log(np.abs(history[:, 1]) + 1e-10) 
    
    plt.plot(x1_vals, x2_ln_abs, marker='o', markersize=4, 
             linestyle='-', color=colors[i], label=f'$\\alpha$ = {alpha}')
    plt.plot(x1_vals[0], x2_ln_abs[0], marker='*', color=colors[i], markersize=12)

plt.title('Task 1: Trajectories in $(x_1, \ln|x_2|)$ Space')
plt.xlabel('$x_1$')
plt.ylabel('$\ln(|x_2|)$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# ==========================================
# Task 2: Rosenbrock 函数优化
# ==========================================
def f2(x1, x2):
    return (1 - x1)**2 + 100 * (x2 - x1**2)**2

def grad_f2(x):
    df_dx1 = -2*(1 - x[0]) - 400*x[0]*(x[1] - x[0]**2)
    df_dx2 = 200*(x[1] - x[0]**2)
    return np.array([df_dx1, df_dx2])

# 为了能清晰看到三条线，设置稍微错开的初始点
initial_points_task2 = [
    [-1.5, 2.0],  # 初始点 A
    [-1.2, 2.5],  # 初始点 B
    [-1.8, 1.5]   # 初始点 C
]
alphas_task2 = [0.0005, 0.0015, 0.002]
histories_task2 = []

print("\n" + "="*60)
print(f"{'Task 2: Rosenbrock Function Optimization Results':^60}")
print("="*60)
print(f"{'Alpha':<8} | {'Init Pt (x1, x2)':<18} | {'Final x1':<9} | {'Final x2':<9} | {'Final f(x)':<12}")
print("-" * 60)

for x0, alpha in zip(initial_points_task2, alphas_task2):
    history = gradient_descent(grad_f2, f2, x0, alpha, iterations=500)
    histories_task2.append(history)
    
    final_x = history[-1]
    final_val = f2(final_x[0], final_x[1])
    init_str = f"({x0[0]}, {x0[1]})"
    print(f"{alpha:<8.4f} | {init_str:<18} | {final_x[0]:<9.5f} | {final_x[1]:<9.5f} | {final_val:<12.6e}")

# 绘制 Task 2: 带有等高线的 2D 轨迹
x1_grid = np.linspace(-2.2, 2.2, 400)
x2_grid = np.linspace(-1.0, 3.5, 400)
X1, X2 = np.meshgrid(x1_grid, x2_grid)
Z = f2(X1, X2)

plt.figure(figsize=(10, 8))
# 使用 log(1+Z) 来让等高线颜色分布更均匀可见
plt.contourf(X1, X2, np.log1p(Z), levels=40, cmap='viridis', alpha=0.8)
plt.colorbar(label='Log(1 + Objective Value)')

for i, (history, alpha) in enumerate(zip(histories_task2, alphas_task2)):
    plt.plot(history[:, 0], history[:, 1], marker='.', markersize=5, 
             linestyle='-', color=colors[i], label=f'$\\alpha$ = {alpha}')
    plt.plot(history[0, 0], history[0, 1], marker='*', color=colors[i], markersize=15)

plt.title('Task 2: Rosenbrock Function Trajectories (Distinct Initial Points)')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
# 限制显示范围，避免个别发散点导致坐标轴被拉伸太大
plt.xlim([-2.2, 2.2])
plt.ylim([-1.0, 3.5])
plt.show()