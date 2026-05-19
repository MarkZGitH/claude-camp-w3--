"""string_utils 的单元测试

每个函数测试三种情况:
- 正常情况(typical case)
- 边界情况(edge case:空串、单字符、大小写、多余空格等)
- 异常情况(invalid input,应抛出 TypeError)
"""

import pytest
from string_utils import reverse_words, count_vowels, is_palindrome


# ============ reverse_words 的 3 个测试 ============

def test_reverse_words_normal():
    """正常情况:多个单词应正确反转"""
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("a b c d") == "d c b a"
    assert reverse_words("Python is fun") == "fun is Python"


def test_reverse_words_edge():
    """边界情况:空串、单词、多余空格"""
    assert reverse_words("") == ""                       # 空字符串
    assert reverse_words("hello") == "hello"             # 单个单词
    assert reverse_words("  hello   world  ") == "world hello"  # 多余空格规范化


def test_reverse_words_invalid_type():
    """异常情况:非字符串输入应抛 TypeError"""
    with pytest.raises(TypeError):
        reverse_words(123)
    with pytest.raises(TypeError):
        reverse_words(None)
    with pytest.raises(TypeError):
        reverse_words(["hello", "world"])


# ============ count_vowels 的 3 个测试 ============

def test_count_vowels_normal():
    """正常情况:混合字母,大小写都要算"""
    assert count_vowels("hello") == 2                    # e, o
    assert count_vowels("AEIOU") == 5                    # 大写元音
    assert count_vowels("Programming") == 3              # o, a, i


def test_count_vowels_edge():
    """边界情况:空、无元音、纯元音"""
    assert count_vowels("") == 0
    assert count_vowels("rhythm") == 0                   # 无元音
    assert count_vowels("aeiouAEIOU") == 10              # 纯元音
    assert count_vowels("12345!@#") == 0                 # 无字母


def test_count_vowels_invalid_type():
    """异常情况:非字符串输入"""
    with pytest.raises(TypeError):
        count_vowels(42)
    with pytest.raises(TypeError):
        count_vowels(None)


# ============ is_palindrome 的 3 个测试 ============

def test_is_palindrome_normal():
    """正常情况:经典回文/非回文"""
    assert is_palindrome("racecar") is True
    assert is_palindrome("level") is True
    assert is_palindrome("hello") is False


def test_is_palindrome_edge():
    """边界情况:空串、单字符、含标点空格"""
    assert is_palindrome("") is True                                       # 空串视为回文
    assert is_palindrome("a") is True                                      # 单字符
    assert is_palindrome("A man, a plan, a canal: Panama") is True         # 含标点
    assert is_palindrome("No 'x' in Nixon") is True                        # 含撇号


def test_is_palindrome_invalid_type():
    """异常情况:数字 12321 看着像回文,但函数只接受字符串"""
    with pytest.raises(TypeError):
        is_palindrome(12321)
    with pytest.raises(TypeError):
        is_palindrome(None)
