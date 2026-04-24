import os
from pathlib import Path

print("=== Day 5 演示前检查 ===\n")

# 检查必需文件
required_files = {
    'movie_analysis_report.html': 'HTML 报告',
    'chart_top10.png': 'Top 10 柱状图',
    'chart_region_pie.png': '地区饼图',
    'chart_yearly_trend.png': '年度趋势折线图',
    'chart_genre_comparison.png': '类型对比柱状图',
    'data_summary.json': '数据摘要',
    'movies_data.csv': '原始数据集'
}

print("1. 文件完整性检查")
print("-" * 50)
all_files_exist = True
for filename, description in required_files.items():
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filename}")
    if not exists:
        all_files_exist = False

if all_files_exist:
    print("\n✓ 所有必需文件都存在")
else:
    print("\n✗ 有文件缺失，请检查")

# 检查文件大小
print("\n2. 文件大小检查")
print("-" * 50)
for filename in required_files.keys():
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        if filename.endswith('.png'):
            size_kb = size / 1024
            print(f"{filename}: {size_kb:.1f} KB")
        elif filename.endswith('.html'):
            size_kb = size / 1024
            print(f"{filename}: {size_kb:.1f} KB")
        else:
            print(f"{filename}: {size} bytes")

# 检查 HTML 内容
print("\n3. HTML 报告内容检查")
print("-" * 50)
if os.path.exists('movie_analysis_report.html'):
    with open('movie_analysis_report.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    checks = {
        'chart_top10.png': 'Top 10 图表引用',
        'chart_region_pie.png': '地区饼图引用',
        'chart_yearly_trend.png': '年度趋势图引用',
        'chart_genre_comparison.png': '类型对比图引用',
        '<table>': '数据表格',
        'Top 5': 'Top 5 标题'
    }

    for check, description in checks.items():
        exists = check in html_content
        status = "✓" if exists else "✗"
        print(f"{status} {description}")

# 数据验证
print("\n4. 数据一致性检查")
print("-" * 50)
import pandas as pd
import json

df = pd.read_csv('movies_data.csv')
with open('data_summary.json', 'r', encoding='utf-8') as f:
    summary = json.load(f)

checks = [
    (len(df), summary['数据集概况']['总电影数'], '总电影数'),
    (round(df['票房'].sum(), 1), summary['数据集概况']['总票房'], '总票房'),
    (df['上映年份'].min(), int(summary['数据集概况']['年份范围'].split('-')[0]), '最早年份'),
    (df['上映年份'].max(), int(summary['数据集概况']['年份范围'].split('-')[1]), '最晚年份')
]

all_consistent = True
for actual, expected, description in checks:
    consistent = actual == expected
    status = "✓" if consistent else "✗"
    print(f"{status} {description}: 实际={actual}, JSON={expected}")
    if not consistent:
        all_consistent = False

if all_consistent:
    print("\n✓ 数据一致性验证通过")
else:
    print("\n✗ 数据不一致，请检查")

# 总结
print("\n" + "="*50)
print("检查总结")
print("="*50)
if all_files_exist and all_consistent:
    print("✓ 所有检查通过，可以开始演示！")
    print("\n下一步：")
    print("1. 在浏览器中打开 movie_analysis_report.html")
    print("2. 找一位非技术同事")
    print("3. 用 5 分钟演示报告")
    print("4. 记录同事的问题和反馈")
else:
    print("✗ 有问题需要修复")
