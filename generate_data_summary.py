import pandas as pd
import json
from datetime import datetime

# 读取数据
df = pd.read_csv('movies_data.csv')

# 生成中间数据产物
data_summary = {
    "生成时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "数据集概况": {
        "总电影数": len(df),
        "年份范围": f"{df['上映年份'].min()}-{df['上映年份'].max()}",
        "总票房": round(df['票房'].sum(), 1),
        "平均票房": round(df['票房'].mean(), 1)
    },
    "Top5电影": [
        {
            "排名": i+1,
            "电影名称": row['电影名称'],
            "票房": round(row['票房'], 1),
            "年份": int(row['上映年份']),
            "类型": row['类型']
        }
        for i, (idx, row) in enumerate(df.nlargest(5, '票房').iterrows())
    ],
    "地区分布": {
        region: round(revenue, 1)
        for region, revenue in df.groupby('地区')['票房'].sum().items()
    },
    "类型分布": {
        genre: {
            "平均票房": round(df[df['类型'] == genre]['票房'].mean(), 1),
            "电影数量": len(df[df['类型'] == genre])
        }
        for genre in df['类型'].unique()
    },
    "年度趋势": {
        int(year): round(avg, 1)
        for year, avg in df.groupby('上映年份')['票房'].mean().items()
    }
}

# 保存为 JSON
with open('data_summary.json', 'w', encoding='utf-8') as f:
    json.dump(data_summary, f, ensure_ascii=False, indent=2)

print("✓ 数据中间产物已保存: data_summary.json")
print(f"\n数据概况:")
print(f"  总电影数: {data_summary['数据集概况']['总电影数']}")
print(f"  年份范围: {data_summary['数据集概况']['年份范围']}")
print(f"  总票房: {data_summary['数据集概况']['总票房']} 百万美元")
print(f"  平均票房: {data_summary['数据集概况']['平均票房']} 百万美元")
