#!/usr/bin/env python
# encoding: utf-8
"""
File Description: https://leetcode-cn.com/problems/two-sum/
Author: rightyonghu
Created Time: 2022/4/16
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for index, num in enumerate(nums):
            left_num = target - num
            if left_num in num_to_index:
                return [index, num_to_index[left_num]]
            num_to_index[num] = index
        return []
