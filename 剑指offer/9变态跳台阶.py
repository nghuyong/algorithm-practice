#!/usr/bin/env python
# encoding: utf-8
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    def jumpFloorII(self, number):
        """
        :param number: 台阶数
        :return: 跳法
        f(n) = f(0) + f(1) + ... + f(n-1) n >= 0
        f(n+1) = f(0) + f(1) + ... + f(n) n >= 0
        f(n+1) - f(n) = f(n) n>=0
        f(n+1) = 2f(n) n>=0
        f(n) = 2^(n-1)
        """
        return 2 ** (number - 1)
