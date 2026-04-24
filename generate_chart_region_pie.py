import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('movies_data.csv')

# 按地区汇总票房
region_revenue = df.groupby('地区')['票房'].sum().sort_values(ascending=False)

print("=== 各地区票房统计 ===")
total_revenue = region_revenue.sum()
for region, revenue in region_revenue.items():
    percentage = revenue / total_revenue * 100
    print(f"{region}: {revenue:.1f} 百万美元 ({percentage:.1f}%)")

print(f"\n总计: {total_revenue:.1f} 百万美元")
print(f"验证: 各地区占比之和 = {(region_revenue.sum() / total_revenue * 100):.1f}%")

# 创建饼图
plt.figure(figsize=(10, 8))

# 计算百分比
percentages = (region_revenue / total_revenue * 100).values

# 绘制饼图
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
wedges, texts, autotexts = plt.pie(
    region_revenue.values,
    labels=region_revenue.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors[:len(region_revenue)],
    textprops={'fontsize': 12, 'weight': 'bold'}
)

# 设置百分比文字样式
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# 设置标题
plt.title('全球票房地区占比 (2009-2022)', fontsize=16, fontweight='bold', pad=20)

# 添加图例，显示具体数值
legend_labels = [f'{region}: {revenue:.1f}M ({revenue/total_revenue*100:.1f}%)'
                 for region, revenue in region_revenue.items()]
plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# 添加业务结论
conclusion = f"全球发行占总票房的 {region_revenue['全球']/total_revenue*100:.1f}%"
plt.text(0, -1.3, conclusion, ha='center', fontsize=11, style='italic', color='#555')

plt.tight_layout()

# 保存图片
plt.savefig('chart_region_pie.png', dpi=300, bbox_inches='tight')
print("\n✓ 饼图已保存为 chart_region_pie.png")

# C3 验证：所有占比加起来应该 = 100%
print(f"\n=== C3 验证 ===")
print(f"所有地区占比之和: {percentages.sum():.2f}%")
if abs(percentages.sum() - 100) < 0.5:
    print("✓ 验证通过：占比之和 = 100%")
else:
    print(f"⚠ 警告：占比之和偏差 {abs(percentages.sum() - 100):.2f}%")
