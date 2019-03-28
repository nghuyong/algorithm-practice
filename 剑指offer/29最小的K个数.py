#!/usr/bin/env python
# encoding: utf-8
"""
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        :param tinput: 整数序列
        :param k: 最小的K个数
        :return:
        """
        if len(tinput) < k or not tinput:
            return []
        tinput.sort()
        return tinput[:k]
