import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('movies_data.csv')

# 获取票房 Top 10
top10 = df.nlargest(10, '票房')[['电影名称', '票房']].sort_values('票房', ascending=False)

# 创建柱状图
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top10)), top10['票房'], color='steelblue')

# 设置 X 轴标签
plt.xticks(range(len(top10)), top10['电影名称'], rotation=45, ha='right')

# 设置标题和标签
plt.title('全球票房 Top 10 电影', fontsize=16, fontweight='bold')
plt.xlabel('电影名称', fontsize=12)
plt.ylabel('票房（百万美元）', fontsize=12)

# 在柱子上显示数值
for i, (idx, row) in enumerate(top10.iterrows()):
    plt.text(i, row['票房'] + 50, f"{row['票房']:.1f}",
             ha='center', va='bottom', fontsize=10)

# 添加网格线
plt.grid(axis='y', alpha=0.3, linestyle='--')

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('chart_top10.png', dpi=300, bbox_inches='tight')
print("✓ 图表已保存为 chart_top10.png")

# 显示 Top 10 数据
print("\n=== Top 10 票房电影 ===")
for i, (idx, row) in enumerate(top10.iterrows(), 1):
    print(f"{i}. {row['电影名称']}: {row['票房']:.1f} 百万美元")
