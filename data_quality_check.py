import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv('movies_data.csv')

print("=== 数据质量检查 ===\n")

# 1. 检查缺失值（NaN）
print("1. 缺失值检查：")
missing = df.isnull().sum()
print(missing)
print(f"\n总缺失值数量: {missing.sum()}")

if missing.sum() > 0:
    print("\n缺失值详情：")
    for col in df.columns:
        if missing[col] > 0:
            print(f"  - {col}: {missing[col]} 个缺失值 ({missing[col]/len(df)*100:.1f}%)")

# 2. 检查重复电影名
print("\n" + "="*50)
print("2. 重复电影名检查：")
duplicates = df[df.duplicated(subset=['电影名称'], keep=False)]
if len(duplicates) > 0:
    print(f"发现 {len(duplicates)} 行重复电影名：")
    print(duplicates[['电影名称', '票房', '上映年份', '地区']].sort_values('电影名称'))
else:
    print("没有发现重复电影名")

# 3. 检查日期格式
print("\n" + "="*50)
print("3. 日期格式检查：")
print(f"上映年份数据类型: {df['上映年份'].dtype}")
print(f"年份范围: {df['上映年份'].min()} - {df['上映年份'].max()}")
print(f"年份样本: {df['上映年份'].head(10).tolist()}")

# 4. 检查票房数据
print("\n" + "="*50)
print("4. 票房数据检查：")
print(f"票房数据类型: {df['票房'].dtype}")
print(f"是否有负数: {'是' if (df['票房'] < 0).any() else '否'}")
print(f"是否有零值: {'是' if (df['票房'] == 0).any() else '否'}")
print(f"最小值: {df['票房'].min()}")
print(f"最大值: {df['票房'].max()}")

# 5. 检查地区分布
print("\n" + "="*50)
print("5. 地区分布：")
region_counts = df['地区'].value_counts()
print(region_counts)

# 6. 检查类型分布
print("\n" + "="*50)
print("6. 类型分布：")
type_counts = df['类型'].value_counts()
print(type_counts)

print("\n" + "="*50)
print("数据质量检查完成！")
