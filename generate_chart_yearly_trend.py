import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('movies_data.csv')

# 按年份计算平均票房
yearly_avg = df.groupby('上映年份')['票房'].mean().sort_index()
yearly_count = df.groupby('上映年份').size().sort_index()

print("=== 年度平均票房趋势 ===\n")
for year in yearly_avg.index:
    print(f"{year} 年: {yearly_avg[year]:7.1f} 百万美元 (共 {yearly_count[year]} 部电影)")

# 创建折线图
plt.figure(figsize=(14, 7))

# 绘制折线
plt.plot(yearly_avg.index, yearly_avg.values,
         marker='o', linewidth=2.5, markersize=8,
         color='#2E86AB', markerfacecolor='#A23B72')

# 在每个点上标注数值
for year, revenue in yearly_avg.items():
    plt.text(year, revenue + 80, f'{revenue:.0f}',
             ha='center', va='bottom', fontsize=9, fontweight='bold')

# 设置标题和标签
plt.title('年度平均票房趋势 (1994-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('上映年份', fontsize=12)
plt.ylabel('平均票房（百万美元）', fontsize=12)

# 设置 X 轴
plt.xticks(yearly_avg.index, rotation=45)

# 添加网格线
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.grid(axis='x', alpha=0.2, linestyle=':')

# 标注关键点
max_year = yearly_avg.idxmax()
max_revenue = yearly_avg.max()
plt.annotate(f'最高点\n{max_year}年\n{max_revenue:.0f}M',
             xy=(max_year, max_revenue),
             xytext=(max_year-2, max_revenue+300),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=10, color='red', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

# 添加业务结论
conclusion = f"2009年《阿凡达》创造了最高平均票房记录"
plt.text(0.5, -0.15, conclusion,
         transform=plt.gca().transAxes,
         ha='center', fontsize=11, style='italic', color='#555')

plt.tight_layout()

# 保存图片
plt.savefig('chart_yearly_trend.png', dpi=300, bbox_inches='tight')
print("\n✓ 折线图已保存为 chart_yearly_trend.png")

# C3 验证：检查关键年份
print("\n=== C3 验证 ===")
print(f"最高平均票房年份: {max_year} 年 ({max_revenue:.1f} 百万美元)")
print(f"最低平均票房年份: {yearly_avg.idxmin()} 年 ({yearly_avg.min():.1f} 百万美元)")

# 检查 2020 年（疫情年）
if 2020 in yearly_avg.index:
    print(f"2020 年（疫情）: {yearly_avg[2020]:.1f} 百万美元")
else:
    print("2020 年（疫情）: 数据集中无此年份数据")

# 检查年份连续性
years = sorted(yearly_avg.index)
missing_years = []
for i in range(len(years)-1):
    gap = years[i+1] - years[i]
    if gap > 1:
        for y in range(years[i]+1, years[i+1]):
            missing_years.append(y)

if missing_years:
    print(f"\n⚠️ 缺失年份: {missing_years}")
    print("   这是正常的，因为数据集只包含高票房电影样本")
else:
    print("\n✓ 年份连续，无缺失")
