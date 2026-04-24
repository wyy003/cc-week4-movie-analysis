import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('movies_data.csv')

print("=== 年度票房趋势分析 - 业务问题探索 ===\n")

# 方案 1：每年总票房
yearly_total = df.groupby('上映年份')['票房'].sum().sort_index()

print("方案 1：每年总票房")
print("-" * 50)
for year, revenue in yearly_total.items():
    count = len(df[df['上映年份'] == year])
    print(f"{year} 年: {revenue:7.1f} 百万美元 ({count} 部电影)")

# 方案 2：每年平均票房
yearly_avg = df.groupby('上映年份')['票房'].mean().sort_index()

print("\n方案 2：每年平均票房")
print("-" * 50)
for year, revenue in yearly_avg.items():
    count = len(df[df['上映年份'] == year])
    print(f"{year} 年: {revenue:7.1f} 百万美元 (平均，共 {count} 部)")

# 方案 3：每年电影数量
yearly_count = df.groupby('上映年份').size().sort_index()

print("\n方案 3：每年电影数量")
print("-" * 50)
for year, count in yearly_count.items():
    print(f"{year} 年: {count} 部电影")

print("\n" + "="*60)
print("业务分析建议：")
print("="*60)
print("\n方案 1（每年总票房）的问题：")
print("  - 数据集中每年电影数量不同（1-4 部）")
print("  - 电影多的年份总票房自然高，不能反映真实趋势")
print("  - 比如 2015 年有 4 部电影，总票房高但不代表市场好")

print("\n方案 2（每年平均票房）的优势：")
print("  - 消除了电影数量的影响")
print("  - 能更准确反映每部电影的市场表现")
print("  - 适合回答'哪一年的电影最卖座'")

print("\n方案 3（每年电影数量）的意义：")
print("  - 反映数据集的覆盖情况")
print("  - 但这个数据集不是完整的市场数据，只是 Top 电影样本")

print("\n推荐：使用方案 2（每年平均票房）")
print("原因：数据集是精选的高票房电影，平均值更能反映趋势")
