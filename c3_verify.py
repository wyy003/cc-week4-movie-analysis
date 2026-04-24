import pandas as pd
import random

# 读取数据
df = pd.read_csv('movies_data.csv')

# 随机选择一部电影
random_movie = df.sample(1).iloc[0]

print("=== C3 验证 - 随机抽取电影 ===\n")
print(f"电影名称: {random_movie['电影名称']}")
print(f"票房: {random_movie['票房']} 百万美元")
print(f"地区: {random_movie['地区']}")
print(f"上映年份: {random_movie['上映年份']}")
print(f"类型: {random_movie['类型']}")
print(f"评分: {random_movie['评分']}")

print("\n" + "="*50)
print("请手动验证以下内容：")
print("="*50)

# 验证 1：这部电影在数据集中的票房
print(f"\n1. 验证票房数据")
print(f"   脚本显示《{random_movie['电影名称']}》票房: {random_movie['票房']} 百万美元")
print(f"   请在 movies_data.csv 文件中查找这部电影，确认票房数字是否一致")

# 验证 2：同地区电影的总票房
same_region = df[df['地区'] == random_movie['地区']]
region_total = same_region['票房'].sum()
region_count = len(same_region)

print(f"\n2. 验证地区汇总")
print(f"   地区: {random_movie['地区']}")
print(f"   该地区电影数量: {region_count} 部")
print(f"   该地区总票房: {region_total:.1f} 百万美元")
print(f"   该地区平均票房: {region_total/region_count:.1f} 百万美元")

print(f"\n   该地区所有电影：")
for idx, row in same_region.iterrows():
    print(f"   - {row['电影名称']}: {row['票房']} 百万美元")

# 验证 3：同类型电影的统计
same_type = df[df['类型'] == random_movie['类型']]
type_total = same_type['票房'].sum()
type_count = len(same_type)

print(f"\n3. 验证类型汇总")
print(f"   类型: {random_movie['类型']}")
print(f"   该类型电影数量: {type_count} 部")
print(f"   该类型总票房: {type_total:.1f} 百万美元")
print(f"   该类型平均票房: {type_total/type_count:.1f} 百万美元")

print("\n" + "="*50)
print("C3 验证说明：")
print("="*50)
print("请用计算器或 Excel 手动计算上述数字，确认脚本输出是否正确。")
print("如果发现差异，记录到协作日志中。")
