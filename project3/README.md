# 项目 3:带单元测试的字符串工具库

Week 3 学习作业 - 函数 + 测试 + 文档完整闭环。

## 功能

提供三个常用字符串工具函数,带完整的 pytest 单元测试和网页实验室。

### 三个核心函数

| 函数 | 输入 | 输出 | 说明 |
|------|------|------|------|
| `reverse_words(s)` | 字符串 | 字符串 | 反转单词顺序,多余空格被规范化 |
| `count_vowels(s)` | 字符串 | 整数 | 统计元音(a/e/i/o/u),不区分大小写 |
| `is_palindrome(s)` | 字符串 | 布尔 | 判断是否回文,忽略大小写和非字母数字 |

所有函数都做**输入类型验证**:非字符串输入会抛 `TypeError`。

## 文件说明

| 文件 | 说明 |
|------|------|
| `string_utils.py` | 三个工具函数(74 行,含完整 docstring) |
| `test_string_utils.py` | pytest 测试套件(9 个测试用例) |
| `index.html` | 网页实验室(Apple 风格,实时演示三个函数) |

## 运行方式

### 使用工具函数
```python
from string_utils import reverse_words, count_vowels, is_palindrome

reverse_words("hello world")       # 'world hello'
count_vowels("Programming")        # 3
is_palindrome("racecar")           # True
```

### 网页实验室
直接在浏览器打开 `index.html`,输入任意字符串:
- 三个函数实时计算结果
- 元音字母会被高亮
- 回文判断会显示"清理后"和"反向"对照
- 自带 5 个示例可一键填入

### 运行测试
```bash
pip install pytest
pytest -v
```

预期输出:
```
test_string_utils.py::test_reverse_words_normal       PASSED
test_string_utils.py::test_reverse_words_edge         PASSED
test_string_utils.py::test_reverse_words_invalid_type PASSED
test_string_utils.py::test_count_vowels_normal        PASSED
test_string_utils.py::test_count_vowels_edge          PASSED
test_string_utils.py::test_count_vowels_invalid_type  PASSED
test_string_utils.py::test_is_palindrome_normal       PASSED
test_string_utils.py::test_is_palindrome_edge         PASSED
test_string_utils.py::test_is_palindrome_invalid_type PASSED
============== 9 passed in 0.02s ==============
```

## 测试策略

每个函数 3 个测试函数,覆盖工业界三大类用例:

| 类型 | 测什么 | 例子 |
|------|--------|------|
| **正常情况** | 典型用法,该工作 | `reverse_words("hello world") == "world hello"` |
| **边界情况** | 空串、单字符、特殊输入 | `count_vowels("") == 0`、`is_palindrome("a") is True` |
| **异常情况** | 错误输入应抛错 | `reverse_words(123)` 抛 `TypeError` |

> 💡 这套"三类用例"心法就是 LLM 工程里 **validation-retry loop** 的源头 ——
> 你能预想到的错误,就能在测试里写出来;能在测试里写出来的错误,
> 就能在生产环境里捕获并处理。

## 学到的知识点

- 函数的**输入类型验证**(`isinstance` + `raise TypeError`)
- 写规范的 **docstring**(Args / Returns / Raises / Examples)
- **pytest 三件套**:`assert` + `pytest.raises` + 测试命名规范
- "**函数 + 测试 + 文档**"三位一体的专业开发流程
- 字符串处理常用技巧:`split()`、`[::-1]`、`isalnum()`、生成器表达式
