#!/usr/bin/env python
# encoding: utf-8
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        """
        :param n: 一个整数
        :return: 二进制中1的个数
        """
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count
