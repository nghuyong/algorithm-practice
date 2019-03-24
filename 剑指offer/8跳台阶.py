#!/usr/bin/env python
# encoding: utf-8
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


class Solution:
    def jumpFloor(self, number):
        """
        :param number: 台阶树木
        :return: 跳法
        """
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        prepre, pre = 1, 2
        for k in range(3, number + 1):
            prepre, pre = pre, prepre + pre
        return pre
