# Week 4 电影票房数据分析项目

## 项目概述

本项目对 1994-2022 年间 30 部高票房电影进行数据分析和可视化，生成包含 4 张图表的完整 HTML 报告。

## 核心结论

1. **票房冠军**：阿凡达以 2847.2 百万美元位居榜首
2. **地区分布**：全球发行电影占总票房的 83.8%，北美发行占 16.2%
3. **历史趋势**：2009 年因《阿凡达》创下最高平均票房记录
4. **类型表现**：科幻和动作类型电影在高票房榜单中表现突出
5. **数据覆盖**：数据集涵盖 1994-2022 年，总票房 44,515.5 百万美元

## 数据来源

- 数据集：`movies_data.csv`
- 包含字段：电影名称、票房、地区、上映年份、类型、评分
- 样本数量：30 部电影

## 可视化图表

1. **Top 10 票房电影柱状图** (`chart_top10.png`)
   - 展示票房最高的 10 部电影排名

2. **各地区票房占比饼图** (`chart_region_pie.png`)
   - 对比全球发行 vs 北美发行的票房占比

3. **年度平均票房趋势折线图** (`chart_yearly_trend.png`)
   - 展示 1994-2022 年的票房趋势变化

4. **各类型电影平均票房对比柱状图** (`chart_genre_comparison.png`)
   - 对比不同类型电影的平均票房表现

## 查看报告

打开 `movie_analysis_report.html` 即可查看完整的分析报告。

## 项目结构

```
cc-week4-movie-analysis/
├── movies_data.csv                      # 原始数据集
├── data_summary.json                    # 数据中间产物
├── movie_analysis_report.html           # 最终报告
├── chart_top10.png                      # 图表 1
├── chart_region_pie.png                 # 图表 2
├── chart_yearly_trend.png               # 图表 3
├── chart_genre_comparison.png           # 图表 4
├── check_data.py                        # 数据检查脚本
├── generate_*.py                        # 各图表生成脚本
├── c3_verify_*.py                       # C3 验证脚本
└── daily_log_day*.md                    # 每日协作日志
```

## 技术栈

- Python 3.x
- pandas - 数据处理
- matplotlib - 数据可视化
- HTML/CSS - 报告展示

## 开发日志

- **Day 1**: 数据概念学习 + 第 1 张图（Top 10 柱状图）
- **Day 2**: 数据质量检查 + 第 2 张图（地区饼图）
- **Day 3**: 趋势分析 + 第 3 张图（年度折线图）
- **Day 4**: 类型对比 + 第 4 张图 + HTML 报告生成

## 数据验证

所有数据均通过 C3 验证：
- ✅ 数字汇总与原始数据一致
- ✅ 图表数据准确无误
- ✅ 报告结论基于真实数据

## 作者

- Wyy
- Co-Authored-By: Claude Sonnet 4.6

## 生成时间

2026-04-24
