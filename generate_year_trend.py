import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('movies_data.csv')

year_stats = df.groupby('上映年份').agg({
    '票房': ['count', 'sum', 'mean']
}).round(2)

year_stats.columns = ['电影数量', '总票房', '平均票房']
year_stats = year_stats.reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(year_stats['上映年份'], year_stats['电影数量'], marker='o', linewidth=2, markersize=8)
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('电影数量', fontsize=12)
ax1.set_title('各年份电影数量趋势', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

ax2.plot(year_stats['上映年份'], year_stats['平均票房'], marker='s', linewidth=2, markersize=8, color='green')
ax2.set_xlabel('年份', fontsize=12)
ax2.set_ylabel('平均票房 (亿美元)', fontsize=12)
ax2.set_title('各年份平均票房趋势', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('year_trend.png', dpi=150, bbox_inches='tight')
print("年份趋势图已生成: year_trend.png")
print("\n年份统计:")
print(year_stats.to_string(index=False))
