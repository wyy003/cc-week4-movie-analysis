import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('movies_data.csv')

# 获取票房 Top 10
top10 = df.nlargest(10, '票房')[['电影名称', '票房']].reset_index(drop=True)

# 创建柱状图
plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top10)), top10['票房'], color='steelblue')

# 设置 x 轴标签
plt.xticks(range(len(top10)), top10['电影名称'], rotation=45, ha='right')

# 添加标题和标签
plt.title('Top 10 票房电影', fontsize=16, fontweight='bold')
plt.xlabel('电影名称', fontsize=12)
plt.ylabel('票房（百万美元）', fontsize=12)

# 在柱子上显示数值
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom', fontsize=10)

# 添加网格线
plt.grid(axis='y', alpha=0.3, linestyle='--')

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('top10_boxoffice.png', dpi=300, bbox_inches='tight')
print("✅ 图片已保存为 top10_boxoffice.png")

# 显示图片
plt.show()

# 打印 Top 10 数据用于验证
print("\n=== Top 10 票房电影数据 ===")
print(top10.to_string(index=False))
