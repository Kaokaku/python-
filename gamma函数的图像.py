import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad  # 数值积分工具



# Gamma 函数的定义式：Γ(x) = ∫₀^∞ t^(x-1) * e^(-t) dt  （仅对 x > 0 收敛）
def my_gamma(x):
    f = lambda t: t**(x - 1) * np.exp(-t)  # 被积函数
    return quad(f, 0, np.inf)[0]           # 在 [0, +∞) 上积分，取结果部分

x = np.linspace(0.01, 5.7, 500)
y = np.array([my_gamma(xi) for xi in x])  # quad 只能对标量积分，逐点计算

plt.figure(figsize=(8, 14))

plt.plot(x, y, label=r'$y = \Gamma(x) = \int_{0}^{+\infty} t^{x-1}e^{-t}\,dt$')  # 绘制 gamma 函数曲线
plt.axhline(0, color='gray', linewidth=1)  # 画一条 y=0 的水平灰色细线，作为 x 轴
plt.axvline(0, color='gray', linewidth=1)  # 画一条 x=0 的垂直灰色细线，作为 y 轴
plt.xlabel('x')  # 设置横轴的标签文字为 "x"
plt.ylabel('y')  # 设置纵轴的标签文字为 "y"
plt.title('Gamma Function')  # 设置图像标题
plt.legend()  # 显示图例（即 plot 中 label 参数对应的说明文字）
plt.grid(True)  # 打开网格线，便于读数
plt.show()  # 弹出窗口显示绘制好的图像（程序会在此暂停，直到关闭窗口）