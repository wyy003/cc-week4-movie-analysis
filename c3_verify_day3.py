import pandas as pd
import random

# 读取数据
df = pd.read_csv('movies_data.csv')

print("=== Day 3 C3 验证：年度平均票房计算 ===\n")

# 随机选择一个年份进行手动验证
available_years = df['上映年份'].unique()
random_year = random.choice(available_years)

print(f"随机选中年份: {random_year}")
print("\n请手动验证以下计算：\n")

# 筛选该年份的电影
year_movies = df[df['上映年份'] == random_year]

print(f"【{random_year} 年的电影列表】")
for idx, row in year_movies.iterrows():
    print(f"  - {row['电影名称']}: {row['票房']:.1f} 百万美元")

# 计算平均票房
total_revenue = year_movies['票房'].sum()
count = len(year_movies)
avg_revenue = year_movies['票房'].mean()

print(f"\n【计算过程】")
print(f"  总票房 = {' + '.join([f'{x:.1f}' for x in year_movies['票房']])} = {total_revenue:.1f}")
print(f"  电影数量 = {count}")
print(f"  平均票房 = {total_revenue:.1f} / {count} = {avg_revenue:.1f} 百万美元")

print(f"\n【验证结果】")
print(f"  pandas 计算结果: {avg_revenue:.1f}")
print(f"  请用计算器验证: {total_revenue:.1f} ÷ {count} = ?")

# 额外验证：检查是否有异常值
print(f"\n【异常值检查】")
max_movie = year_movies.loc[year_movies['票房'].idxmax()]
min_movie = year_movies.loc[year_movies['票房'].idxmin()]
print(f"  最高票房: {max_movie['电影名称']} ({max_movie['票房']:.1f})")
print(f"  最低票房: {min_movie['电影名称']} ({min_movie['票房']:.1f})")
print(f"  差距: {max_movie['票房'] - min_movie['票房']:.1f} 百万美元")

if count == 1:
    print(f"\n⚠️ 注意: {random_year} 年只有 1 部电影，平均值 = 该电影票房")
