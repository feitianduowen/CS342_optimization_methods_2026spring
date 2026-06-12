import numpy as np
import matplotlib.pyplot as plt

# 1. 定义目标函数
def f(x1, x2):
    return (1-x1)**2 + 100*(x2-x1**2)**2

# 2. 定义梯度函数 (计算偏导数)
def grad_f(x1, x2):
    df_dx1 = -2*(1-x1) - 400*x1*(x2-x1**2)
    df_dx2 = 200*(x2-x1**2)
    return df_dx1, df_dx2

# 3. 生成二维网格数据
# 在 [-5, 5] 范围内生成 400x400 的密集网格用于绘制平滑的颜色背景
x1 = np.linspace(-5, 5, 400)
x2 = np.linspace(-5, 5, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)

# 4. 创建画布
plt.figure(figsize=(10, 8))

# 5. 绘制彩色填充的等高线图 (背景颜色表示函数值大小)
# levels 控制颜色的层数，cmap 指定颜色映射表 (例如 'viridis', 'plasma', 'coolwarm')
contour_filled = plt.contourf(X1, X2, Z, levels=50, cmap='viridis')

# 添加颜色条标尺
plt.colorbar(contour_filled, label='Objective Value $f(x)$')

# 叠加基础的等高线线条，增加立体感
plt.contour(X1, X2, Z, levels=10, colors='black', linewidths=0.8, alpha=1)

# 6. 绘制梯度向量箭头 (使用 quiver)
# 为了避免箭头过于密集，使用步长 (step) 对网格进行降采样
step = 20
X1_sub = X1[::step, ::step]
X2_sub = X2[::step, ::step]
U, V = grad_f(X1_sub, X2_sub)

# 绘制负梯度方向（即指向最小值的最速下降方向），若要绘制正梯度方向去掉负号即可
plt.quiver(X1_sub, X2_sub, -U, -V, color='red', width=0.003, scale=200000, label='Negative Gradient')

# 7. 图表格式化
plt.title('2D Contour Map with Gradient Vectors')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)

# 显示图像
plt.show()