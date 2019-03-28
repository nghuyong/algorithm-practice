#!/usr/bin/env python
# encoding: utf-8
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        :param numbers: 输入的数组
        :return:
        """
        if not numbers:
            return 0
        current_num = numbers[0]
        count = 1
        for index in range(1,len(numbers)):
            if numbers[index] == current_num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    current_num = numbers[index]
                    count = 1
        if count > 0:
            # check 一下
            final_count = 0
            for num in numbers:
                if num == current_num:
                    final_count += 1
            if final_count * 2 > len(numbers):
                return current_num
        return 0
