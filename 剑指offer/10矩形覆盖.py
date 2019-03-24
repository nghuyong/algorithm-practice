#!/usr/bin/env python
# encoding: utf-8
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
    def rectCover(self, number):
        """
        :param number: 小的矩形的个数
        :return: 总共的方法
        f(n) = f(n-1) + f(n-2)
        """
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        prepre, pre = 1, 2
        for k in range(3, number + 1):
            prepre, pre = pre, pre + prepre
        return pre
