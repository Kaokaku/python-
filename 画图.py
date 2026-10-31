import numpy as np  # 导入 numpy 数值计算库，并起别名 np，用于生成采样点和计算函数值
import matplotlib.pyplot as plt  # 导入 matplotlib 的 pyplot 绘图模块，并起别名 plt，用于画图

x = np.linspace(-3, 3, 500)  # 在 -5 到 5 之间均匀生成 500 个 x 值，点越多曲线越平滑
y1 = np.sinh(x)  # 对每个 x 值计算双曲正弦 sinh(x)
y2 = np.cosh(x)  # 对每个 x 值计算双曲余弦 cosh(x)
y3=np.exp(x)*0.5

plt.figure(figsize=(8, 14))  # 设置画布大小为 宽12英寸、高6英寸（数值越大图越大，改变宽度即可让图变宽）

plt.plot(x, y1, label=r'$y = \sinh(x)$')  # 绘制第一条曲线 sinh(x)，并设置图例标签（LaTeX 格式）
plt.plot(x, y2, label=r'$y = \cosh(x)$')  # 再次调用 plot，第二条曲线会画在同一个坐标轴上
plt.plot(x, y3, label=r'$y = \dfrac{1}{2}e^x$')
plt.axhline(0, color='gray', linewidth=1)  # 画一条 y=0 的水平灰色细线，作为 x 轴
plt.axvline(0, color='gray', linewidth=1)  # 画一条 x=0 的垂直灰色细线，作为 y 轴
plt.xlabel('x')  # 设置横轴的标签文字为 "x"
plt.ylabel('y')  # 设置纵轴的标签文字为 "y"
plt.title('Hyperbolic Function')  # 设置图像标题为 "Hyperbolic Sine Function"（双曲正弦函数）
plt.legend()  # 显示图例（即 plot 中 label 参数对应的说明文字）
plt.grid(True)  # 打开网格线，便于读数
plt.show()  # 弹出窗口显示绘制好的图像（程序会在此暂停，直到关闭窗口）
