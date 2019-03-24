#!/usr/bin/env python
# encoding: utf-8
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


class Solution:
    def Fibonacci(self, n):
        """
        :param n: 整数n
        :return: 数列第n项的数字
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        prepre, pre = 0, 1
        for k in range(2, n + 1):
            prepre, pre = pre, pre + prepre
        return pre
