import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('demo_movies.csv')

# 显示基本信息
print("=== 数据集基本信息 ===")
print(f"总行数: {len(df)}")
print(f"总列数: {len(df.columns)}")
print(f"列名: {list(df.columns)}")
print()

# 显示每列的前 5 行
print("=== 前 5 行数据 ===")
print(df.head(5))
print()

# 显示每列的数据类型
print("=== 每列的数据类型 ===")
print(df.dtypes)
