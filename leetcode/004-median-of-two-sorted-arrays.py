#!/usr/bin/env python
# encoding: utf-8
"""
File Description: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
Author: rightyonghu
Created Time: 2022/4/16
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 先归并排序
        merged_num_index = -1
        i, j = 0, 0
        all_num_count = len(nums1) + len(nums2)
        last_num_1, last_num_2 = None, None
        while i < len(nums1) or j < len(nums2):
            a = nums1[i] if i < len(nums1) else 10 ** 7
            b = nums2[j] if j < len(nums2) else 10 ** 7
            if a < b:
                merged_num_index += 1
                last_num_2 = last_num_1
                last_num_1 = a
                i += 1
            else:
                last_num_2 = last_num_1
                last_num_1 = b
                merged_num_index += 1
                j += 1
            if all_num_count % 2 == 1 and merged_num_index == (all_num_count - 1) // 2:
                return last_num_1
            if all_num_count % 2 == 0 and merged_num_index == all_num_count // 2:
                return (last_num_1 + last_num_2) / 2
