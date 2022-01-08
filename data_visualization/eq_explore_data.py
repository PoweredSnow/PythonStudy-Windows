import json
import plotly.express as px
import pandas as pd

# 探索数据的结构。
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=2)

# 创建地震列表
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# 提取震级
# mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
# print(mags[:10])

# 提取标题
eq_title = all_eq_data['metadata']['title']

# 提取震级和位置数据
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

# print(mags[:10])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])

data = pd.DataFrame(
    data=zip(mags, titles, lons, lats), columns=['震级', '位置', '经度', '纬度']
)
data.head()

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=eq_title,
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()
