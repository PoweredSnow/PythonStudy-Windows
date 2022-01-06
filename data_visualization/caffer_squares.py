import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# scatter() 绘制单个点
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# ax.scatter(x_values, y_values, c='red', s=10)

# 设置图表标题并给坐标轴加上标签。
ax.set_title('Square number', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('The square of the value', fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小4。
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()

# 自动将图表保存到文件中
plt.savefig('squares_plot.png', bbox_inches='tight')
