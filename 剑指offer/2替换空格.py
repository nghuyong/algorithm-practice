#!/usr/bin/env python
# encoding: utf-8
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replaceSpace(s):
    """
    :param s: 输入字符串
    :return: 替换空格以后输出的字符串
    """
    return s.replace(' ', '%20')
