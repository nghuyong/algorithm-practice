#!/usr/bin/env python
# encoding: utf-8
"""
汇编语言中有一种移位指令叫做循环左移（ROL），
现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""


class Solution:
    def LeftRotateString(self, s, n):
        """
        :param s: 字符串
        :param n: 左移位数
        :return: 移动后的字符串
        YX = (X^TY^T)^T
        """
        if not s:
            return ""
        if n < 0:
            raise Exception('error')
        s = list(s)
        n = n % len(s)
        self.swap_array(s, 0, n - 1)
        self.swap_array(s, n, len(s) - 1)
        self.swap_array(s, 0, len(s) - 1)
        return "".join(s)

    def swap_array(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
