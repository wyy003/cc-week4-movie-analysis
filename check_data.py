import pandas as pd

# 读取数据集
df = pd.read_csv('movies_data.csv')

# 显示基本信息
print("=== 数据集基本信息 ===")
print(f"总行数: {len(df)}")
print(f"总列数: {len(df.columns)}")
print(f"列名: {list(df.columns)}")
print()

# 显示前 10 行
print("=== 前 10 行数据 ===")
print(df.head(10))
print()

# 显示数据类型
print("=== 每列的数据类型 ===")
print(df.dtypes)
print()

# 显示一些统计信息
print("=== 票房统计 ===")
print(f"总票房: {df['票房'].sum():.1f} 百万美元")
print(f"平均票房: {df['票房'].mean():.1f} 百万美元")
print(f"最高票房: {df['票房'].max():.1f} 百万美元")
print()

print("=== 票房 Top 5 电影 ===")
top5 = df.nlargest(5, '票房')[['电影名称', '票房', '上映年份']]
print(top5.to_string(index=False))
