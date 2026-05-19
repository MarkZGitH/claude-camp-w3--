# 项目 2:JSON 配置文件读写器

Week 3 学习作业 - 文件 I/O 完整生命周期(读取 → 修改 → 验证 → 写回)。

## 功能

提供两种形态:

- **命令行版**(`config_editor.py`):菜单式交互,适合脚本批处理或终端用户
- **网页版**(`index.html`):Apple 风格 GUI,实时预览 + 下载,适合非技术用户

两种实现**共享同一套验证规则**。

## 配置项与验证规则

| 配置项 | 类型 | 验证规则 |
|--------|------|----------|
| `theme` | 字符串 | 必须是 `light` / `dark` / `auto` 之一 |
| `language` | 字符串 | 必须是 `zh-CN` / `en-US` / `ja-JP` 之一 |
| `font_size` | 整数 | 必须在 8-32 之间 |
| `auto_save` | 布尔 | 接受 true/false/yes/no/1/0 等多种写法 |
| `notifications` | 布尔 | 同上 |

## 文件说明

| 文件 | 说明 |
|------|------|
| `config_editor.py` | 命令行编辑器(84 行) |
| `config.json` | 默认配置文件 |
| `index.html` | 网页可视化编辑器(Apple 风格) |

## 运行方式

### 命令行版
```bash
python config_editor.py
```
菜单交互:输入编号选择配置项,输入新值,系统先验证再保存。

### 网页版
直接在浏览器打开 `index.html`(无需服务器):
- iOS 风格分段控件切换主题/语言
- 滑块调节字体大小
- 开关切换布尔配置
- 实时 JSON 预览
- 一键下载更新后的 `config.json`
- 可加载已有配置文件(带格式验证)

## 操作示例(命令行)

```
============================================
            当前配置
============================================
  1. theme          = light
  2. language       = zh-CN
  3. font_size      = 14
  4. auto_save      = True
  5. notifications  = True
============================================

输入要修改的项目编号(或 q 退出): 3
输入新的 font_size 值 (当前 = 14): 99
⚠️  必须在 8-32 之间,未修改

输入要修改的项目编号(或 q 退出): 3
输入新的 font_size 值 (当前 = 14): 18
✅ 已更新 font_size = 18
```

## 测试方法

用 `printf` 模拟键盘输入,一次性验证多种场景:

```bash
printf "1\ndark\n3\n99\n3\n18\nq\n" | python3 config_editor.py
```

预期:主题改 dark 成功 → font_size=99 被拒 → font_size=18 成功 → 退出。

## 学到的知识点

- `os.path.exists()` 文件存在性检查
- `json.load()` / `json.dump()` 完整读写循环
- `input()` 接收用户输入,`while True` + `break` 实现菜单循环
- 函数返回元组 `(bool, value_or_error)` 表达"成功/失败 + 数据"
- **数据验证模式**:
  - 范围检查(`8 <= x <= 32`)
  - 枚举检查(`x in [...]`)
  - 类型转换 + 多种写法兼容(string → bool)
- **同一业务逻辑双形态交付**:CLI(后端友好)+ Web(用户友好)

> 💡 "先验证再保存"思维就是 LLM 工程中 **validation-retry loop** 的雏形:
> 不信任输入 → 验证 → 不合格则拒绝 → 信号清晰 → 用户重试。
