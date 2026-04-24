import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('movies_data.csv')

# 按类型分组，计算平均票房
genre_avg = df.groupby('类型')['票房'].mean().sort_values(ascending=False)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 创建分组柱状图
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(genre_avg)), genre_avg.values, color='steelblue')

# 设置 x 轴标签
plt.xticks(range(len(genre_avg)), genre_avg.index, rotation=45, ha='right')

# 添加标题和轴标签
plt.title('各类型电影平均票房对比', fontsize=16, fontweight='bold')
plt.xlabel('电影类型', fontsize=12)
plt.ylabel('平均票房（百万美元）', fontsize=12)

# 在柱子上方显示数值
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom', fontsize=10)

# 添加网格线
plt.grid(axis='y', alpha=0.3, linestyle='--')

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('chart_genre_comparison.png', dpi=300, bbox_inches='tight')
print("✓ 图表已保存: chart_genre_comparison.png")

# 输出统计信息
print(f"\n各类型平均票房排名:")
for i, (genre, avg_box) in enumerate(genre_avg.items(), 1):
    count = len(df[df['类型'] == genre])
    print(f"{i}. {genre}: {avg_box:.1f} 百万美元 (样本数: {count})")
