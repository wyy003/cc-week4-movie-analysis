import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('movies_data.csv')

# 类型统计
type_counts = df['类型'].value_counts()
type_boxoffice = df.groupby('类型')['票房'].agg(['sum', 'mean']).round(1)

# 创建双图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 左图：类型数量
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffa07a', '#98d8c8']
bars1 = ax1.bar(type_counts.index, type_counts.values, color=colors)
ax1.set_xlabel('电影类型', fontsize=12)
ax1.set_ylabel('电影数量', fontsize=12)
ax1.set_title('各类型电影数量分布', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=11)

# 右图：类型平均票房
bars2 = ax2.bar(type_boxoffice.index, type_boxoffice['mean'], color=colors)
ax2.set_xlabel('电影类型', fontsize=12)
ax2.set_ylabel('平均票房 (百万美元)', fontsize=12)
ax2.set_title('各类型平均票房', fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

for bar in bars2:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.0f}',
             ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.savefig('type_distribution.png', dpi=300, bbox_inches='tight')
print("✓ 类型分布图已生成: type_distribution.png")

print("\n=== 类型统计 ===")
print(f"{'类型':<8} {'数量':<6} {'总票房':<10} {'平均票房':<10}")
print("-" * 40)
for type_name in type_counts.index:
    count = type_counts[type_name]
    total = type_boxoffice.loc[type_name, 'sum']
    avg = type_boxoffice.loc[type_name, 'mean']
    print(f"{type_name:<8} {count:<6} {total:<10.1f} {avg:<10.1f}")
