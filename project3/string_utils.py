"""字符串工具库 - 三个常用字符串处理函数

每个函数都验证输入类型,非字符串输入会抛 TypeError。
"""


def reverse_words(s):
    """反转字符串中的单词顺序。

    Args:
        s (str): 输入字符串。

    Returns:
        str: 单词顺序反转后的新字符串,多余空格会被规范化为单个空格。

    Raises:
        TypeError: 当输入不是字符串时。

    Examples:
        >>> reverse_words("hello world")
        'world hello'
    """
    if not isinstance(s, str):
        raise TypeError(f"输入必须是字符串,收到 {type(s).__name__}")
    return " ".join(s.split()[::-1])


def count_vowels(s):
    """统计字符串中元音字母的数量(不区分大小写)。

    元音定义:a, e, i, o, u(不包含 y)。

    Args:
        s (str): 输入字符串。

    Returns:
        int: 元音字母总数。

    Raises:
        TypeError: 当输入不是字符串时。

    Examples:
        >>> count_vowels("hello")
        2
    """
    if not isinstance(s, str):
        raise TypeError(f"输入必须是字符串,收到 {type(s).__name__}")
    return sum(1 for c in s.lower() if c in "aeiou")


def is_palindrome(s):
    """判断字符串是否为回文。

    忽略大小写、空格和非字母数字字符。空字符串视为回文。

    Args:
        s (str): 输入字符串。

    Returns:
        bool: 是回文返回 True,否则返回 False。

    Raises:
        TypeError: 当输入不是字符串时。

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
    """
    if not isinstance(s, str):
        raise TypeError(f"输入必须是字符串,收到 {type(s).__name__}")
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
