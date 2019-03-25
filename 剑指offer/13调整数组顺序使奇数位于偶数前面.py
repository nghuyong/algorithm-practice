#!/usr/bin/env python
# encoding: utf-8
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        """
        :param array: 输入的数组
        :return: 调整好顺序的数组
        """
        return sorted(array, key=lambda c: c % 2, reverse=True)
