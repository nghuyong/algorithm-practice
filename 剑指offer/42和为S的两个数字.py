#!/usr/bin/env python
# encoding: utf-8
"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        """
        :param array: 有序数组
        :param tsum: 和
        :return:
        """
        left = 0
        right = len(array) - 1
        result = []
        while left < right:
            if array[left] + array[right] == tsum:
                if not result or result[0] * result[1] > array[left] * array[right]:
                    result = [array[left], array[right]]
                left += 1
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                right -= 1
        return result
