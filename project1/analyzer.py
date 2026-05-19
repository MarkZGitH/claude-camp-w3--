"""
项目 1：CSV 学员数据分析器
Week 3 - 数据处理 + 文件 I/O 练习

业务背景:对赌制度
- active    = 还在进行中,未到截止日期
- completed = 按时完成,老师退费(奖励)
- failed    = 未按时完成,不退费
"""

import pandas as pd
import json

# ---------- 第 1 步:读取 CSV 文件 ----------
df = pd.read_csv("students.csv")

# ---------- 第 2 步:统计总人数 ----------
total_students = len(df)

# ---------- 第 3 步:统计各国家人数 ----------
country_counts = df["country"].value_counts().to_dict()

# ---------- 第 4 步:统计对赌状态分布 ----------
# .get(key, 0) 是为了防止某种状态在数据里一个都没有时报错
status_counts = df["bet_status"].value_counts().to_dict()
active_count = status_counts.get("active", 0)
completed_count = status_counts.get("completed", 0)
failed_count = status_counts.get("failed", 0)

# ---------- 第 5 步:计算两种完成率 ----------
# 总体完成率:分母包含还在进行中的学员(快照视角)
overall_rate = round(completed_count / total_students * 100, 2)

# 已结算完成率:只看已分出胜负的学员(更能反映对赌真实效果)
settled_total = completed_count + failed_count
if settled_total > 0:
    settled_rate = round(completed_count / settled_total * 100, 2)
else:
    settled_rate = 0.0

# ---------- 第 6 步:组装报告 ----------
report = {
    "total_students": total_students,
    "country_distribution": country_counts,
    "bet_status_distribution": {
        "active": active_count,
        "completed": completed_count,
        "failed": failed_count,
    },
    "overall_completion_rate_percent": overall_rate,
    "settled_completion_rate_percent": settled_rate,
}

# ---------- 第 7 步:打印到屏幕 ----------
print("=" * 44)
print("         学员对赌数据分析报告")
print("=" * 44)
print(f"总人数:              {total_students}")
print(f"  ├─ 进行中:         {active_count}")
print(f"  ├─ 完成(可退费):   {completed_count}")
print(f"  └─ 未完成(不退费): {failed_count}")
print(f"\n总体完成率:          {overall_rate}%   (含进行中)")
print(f"已结算完成率:        {settled_rate}%  (仅看已分胜负)")
print("\n各国家人数分布:")
for country, count in country_counts.items():
    print(f"  - {country}: {count}")
print("=" * 44)

# ---------- 第 8 步:保存为 JSON 文件 ----------
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("\n✅ 报告已保存到 report.json")
