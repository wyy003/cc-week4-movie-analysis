import pandas as pd
import random

# 读取数据
df = pd.read_csv('movies_data.csv')

print("=== Day 4 C3 验证：类型平均票房计算 ===\n")

# 随机选择一个类型进行手动验证
available_genres = df['类型'].unique()
random_genre = random.choice(available_genres)

print(f"随机选中类型: {random_genre}")
print("\n请手动验证以下计算：\n")

# 筛选该类型的电影
genre_movies = df[df['类型'] == random_genre]

print(f"【{random_genre}类型的电影列表】")
for idx, row in genre_movies.iterrows():
    print(f"  - {row['电影名称']}: {row['票房']:.1f} 百万美元")

# 计算平均票房
total_revenue = genre_movies['票房'].sum()
count = len(genre_movies)
avg_revenue = genre_movies['票房'].mean()

print(f"\n【计算过程】")
print(f"  总票房 = {' + '.join([f'{x:.1f}' for x in genre_movies['票房']])} = {total_revenue:.1f}")
print(f"  电影数量 = {count}")
print(f"  平均票房 = {total_revenue:.1f} / {count} = {avg_revenue:.1f} 百万美元")

print(f"\n【验证结果】")
print(f"  pandas 计算结果: {avg_revenue:.1f}")
print(f"  请用计算器验证: {total_revenue:.1f} ÷ {count} = ?")

# 额外验证：检查 HTML 报告中的数据
print(f"\n【HTML 报告验证】")
print(f"  请打开 movie_analysis_report.html")
print(f"  检查 Top 5 电影列表是否与数据集一致")
print(f"  检查 4 张图表是否正确显示")

# 验证 JSON 数据
import json
with open('data_summary.json', 'r', encoding='utf-8') as f:
    summary = json.load(f)

print(f"\n【JSON 数据验证】")
print(f"  data_summary.json 中的总电影数: {summary['数据集概况']['总电影数']}")
print(f"  实际数据集行数: {len(df)}")
print(f"  是否一致: {'✓ 是' if summary['数据集概况']['总电影数'] == len(df) else '✗ 否'}")
