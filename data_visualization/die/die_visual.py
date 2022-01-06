from fileinput import filename
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6和一个D10。
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子并将结果存储在一个列表中。
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]
# for roll_num in range(50_000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)


# 分析结果。
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 对结果进行可视化。
x_values = list(range(2, max_result + 1))
# Bar() 用于绘制条形图的数据集
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
# 配置坐标轴
my_layout = Layout(title='掷一个 D6 和一个 D10 50 000 次的结果',
                xaxis=x_axis_config, yaxis=y_axis_config)
# 生成图表
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
