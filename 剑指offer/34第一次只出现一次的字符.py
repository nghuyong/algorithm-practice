#!/usr/bin/env python
# encoding: utf-8
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        :param s: 输入字符串
        :return: 第一个只出现一次的字符
        """
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for index, c in enumerate(s):
            if m[c] == 1:
                return index
        return -1
