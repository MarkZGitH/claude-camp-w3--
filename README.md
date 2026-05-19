# Claude Camp Week 3

数据处理 + 文件 I/O + Git 进阶 + pytest 入门 —— Phase 0 收官周。

## 本周主题

从"玩具数据"升级到"真实业务数据";从"代码能跑"升级到"代码有测试";从"会 push"升级到"会用分支做专业开发"。

## 学习重点

- 用 Pandas 处理真实 CSV 数据,而不是手写循环
- 完成 JSON 文件的完整读写循环(读取 → 修改 → 验证 → 写回)
- 用 **pytest** 写单元测试,覆盖正常 / 边界 / 异常三类用例
- 用 **feature branch + Pull Request** 做专业开发流程
- 同一份业务逻辑两种交付形态:Python(CLI / 后端)+ HTML(GUI / 前端)

## 三个项目

| # | 项目 | 简介 | 代码 | 在线试用 |
|---|------|------|------|----------|
| 1 | **CSV 学员对赌分析器** | 用 Pandas 分析学员对赌数据,输出 JSON 报告;区分"总体完成率"和"已结算完成率"两个业务指标 | [`project1/`](./project1) | [▶️ 打开](https://markzgith.github.io/claude-camp-w3--/project1/) |
| 2 | **JSON 配置编辑器** | 双形态实现:Python CLI 菜单 + iOS 风格 Web 编辑器,共享同一套数据验证规则 | [`project2/`](./project2) | [▶️ 打开](https://markzgith.github.io/claude-camp-w3--/project2/) |
| 3 | **字符串工具库** | 三个工具函数 + 9 个 pytest 测试用例 + Apple Playgrounds 风格 Web 实验室 | [`project3/`](./project3) | [▶️ 打开](https://markzgith.github.io/claude-camp-w3--/project3/) |

## 本周新解锁的技能

### Python 层面
- Pandas:`read_csv` / `value_counts` / 布尔过滤
- 文件 I/O 完整生命周期(`os.path.exists` + `json.load` / `json.dump`)
- 交互式 CLI(`input` + `while True` 菜单循环)
- 数据验证模式(范围 / 枚举 / 类型转换)
- **pytest 三件套**:`assert` + `pytest.raises` + 测试命名规范
- 函数 + docstring + 测试三位一体

### Git 层面
- `git checkout -b feature/xxx` 创建 feature 分支
- `git push -u origin <分支>` 推送新分支并建立追踪
- GitHub Pull Request 流程(开 PR → review → merge → delete branch)
- `git checkout <文件>` 撤销本地未提交改动

### 前端层面(Apple 设计语言)
- 系统字体栈 `-apple-system, BlinkMacSystemFont, "SF Pro Display"`
- iOS 控件复刻:分段控件、Toggle 开关、滑块
- 克制的动效(`fadeUp` + 卡片悬浮)
- 8pt 间距网格 + `letter-spacing: -0.022em` 标志性字距

## 仓库结构

```
claude-camp-w3--/
├── README.md              ← 你正在看的文件
├── .gitignore
├── project1/              ← CSV 分析器
│   ├── analyzer.py
│   ├── students.csv
│   ├── report.json
│   ├── index.html
│   └── README.md
├── project2/              ← JSON 配置编辑器
│   ├── config_editor.py
│   ├── config.json
│   ├── index.html
│   └── README.md
└── project3/              ← 字符串工具库
    ├── string_utils.py
    ├── test_string_utils.py
    ├── index.html
    └── README.md
```

## 本地运行

```bash
# 克隆仓库
git clone https://github.com/MarkZGitH/claude-camp-w3--.git
cd claude-camp-w3--

# 安装依赖
pip3 install pandas pytest

# 运行任意项目(以 project3 为例)
cd project3
python3 -m pytest -v        # 跑测试
open index.html             # 打开网页实验室
```

## 进度

```
Phase 0 - Python 打底阶段
├── ✅ Week 1: Git 基础 + Python 语法
├── ✅ Week 2: 函数 + 模块
└── ✅ Week 3: 数据处理 + pytest + 分支工作流  ← 完成

Next: Phase 1 - Partner Learning Path 四模块
```
