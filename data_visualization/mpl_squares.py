import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
# subplots() 在一张图片中绘制一个或多个图表
fig, ax = plt.subplots()
# plot() 根据给定的数据以有意义的方式绘制图表
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("Square number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("The square of the value", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)

plt.show()
