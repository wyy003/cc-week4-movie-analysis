import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('movies_data.csv')

region_counts = df['地区'].value_counts()

plt.figure(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff']
explode = (0.05, 0)

plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%',
        startangle=90, colors=colors, explode=explode, textprops={'fontsize': 14})
plt.title('电影地区分布', fontsize=16, pad=20)

plt.savefig('region_distribution.png', dpi=300, bbox_inches='tight')
print("✓ 饼图已生成: region_distribution.png")
print(f"\n地区统计:")
for region, count in region_counts.items():
    print(f"  {region}: {count}部 ({count/len(df)*100:.1f}%)")
