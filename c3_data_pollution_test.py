import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=== Day 2 C3 验证：故意污染数据测试 ===\n")

# 读取原始数据
df_original = pd.read_csv('movies_data.csv')

# 测试 1：把一行的"全球"改成"全球 "（带空格）
print("测试 1：地区名称带空格")
df_test1 = df_original.copy()
df_test1.loc[0, '地区'] = '全球 '  # 阿凡达的地区改成带空格

region_revenue_original = df_original.groupby('地区')['票房'].sum()
region_revenue_test1 = df_test1.groupby('地区')['票房'].sum()

print("原始数据地区分布：")
print(region_revenue_original)
print(f"\n污染后地区分布：")
print(region_revenue_test1)

if len(region_revenue_test1) > len(region_revenue_original):
    print(f"\n⚠️ 发现问题：地区数量从 {len(region_revenue_original)} 变成 {len(region_revenue_test1)}")
    print(f"   '全球 '（带空格）被当成了新地区")
    print(f"   '全球'票房从 {region_revenue_original['全球']:.1f} 减少到 {region_revenue_test1.get('全球', 0):.1f}")
else:
    print("\n✓ 没有发现问题")

# 测试 2：把一行的票房改成 NaN
print("\n" + "="*60)
print("测试 2：票房数据变成 NaN")
df_test2 = df_original.copy()
df_test2.loc[0, '票房'] = None  # 阿凡达的票房改成 NaN

total_original = df_original['票房'].sum()
total_test2 = df_test2['票房'].sum()

print(f"原始总票房: {total_original:.1f} 百万美元")
print(f"污染后总票房: {total_test2:.1f} 百万美元")
print(f"差异: {total_original - total_test2:.1f} 百万美元")

if abs(total_original - total_test2) > 1:
    print(f"\n⚠️ 发现问题：总票房减少了 {total_original - total_test2:.1f}")
    print(f"   这是因为 NaN 值在求和时被忽略了")
else:
    print("\n✓ 没有发现问题")

# 测试 3：把一行的电影名改成繁体
print("\n" + "="*60)
print("测试 3：电影名改成繁体")
df_test3 = df_original.copy()
df_test3.loc[0, '电影名称'] = '阿凡達'  # 简体改繁体

top5_original = df_original.nlargest(5, '票房')['电影名称'].tolist()
top5_test3 = df_test3.nlargest(5, '票房')['电影名称'].tolist()

print(f"原始 Top 5: {top5_original}")
print(f"污染后 Top 5: {top5_test3}")

if top5_original[0] != top5_test3[0]:
    print(f"\n⚠️ 发现问题：第一名从 '{top5_original[0]}' 变成 '{top5_test3[0]}'")
    print(f"   虽然票房数据没变，但电影名显示不一致")
else:
    print("\n✓ 电影名一致")

print("\n" + "="*60)
print("C3 验证总结：")
print("="*60)
print("1. 地区名称的空格会导致分组错误，产生新的地区类别")
print("2. NaN 值会在求和时被自动忽略，导致总数减少")
print("3. 电影名的繁简体不影响排序，但会影响显示")
print("\n建议：数据清洗时需要处理：")
print("  - 去除字段前后的空格（strip）")
print("  - 明确 NaN 值的处理规则（删除/填充/标记）")
print("  - 统一文字编码（简体/繁体）")
