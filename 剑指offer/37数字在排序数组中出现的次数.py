#!/usr/bin/env python
# encoding: utf-8
"""
统计一个数字在排序数组中出现的次数。
"""


class Solution:
    def GetNumberOfK(self, data, k):
        """
        :param data: 有序的数组
        :param k: 数字k
        :return:
        """
        if not data:
            return 0
        index = self.binary_search(data, k)
        if index == -1:
            return 0
        # 向左搜寻
        left = index
        while left >= 0 and data[left] == k:
            left -= 1
        # 向右搜寻
        right = index
        while right < len(data) and data[right] == k:
            right += 1
        return (right - 1) - (left + 1) + 1

    @staticmethod
    def binary_search(data, k):
        start = 0
        end = len(data) - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k:
                return mid
            elif data[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
        return -1
