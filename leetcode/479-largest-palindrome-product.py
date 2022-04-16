#!/usr/bin/env python
# encoding: utf-8
"""
File Description:https://leetcode-cn.com/problems/largest-palindrome-product/submissions/
Author: rightyonghu
Created Time: 2022/4/16
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        # n * n < 10^n * 10^n = 10^2n - 1
        right_half_num = 10 ** n - 1
        right_half_num_min = 10 ** (n - 1) + 1
        while right_half_num >= right_half_num_min:
            # 构建all num
            temp = right_half_num
            all_num = right_half_num * (10 ** n)
            n_count = n - 1
            while temp:
                all_num += (temp % 10) * (10 ** n_count)
                n_count -= 1
                temp = temp // 10
            # 寻找 all num 是否可以是两个 n 位数的和
            x = 10 ** n - 1
            while x * x >= all_num:
                if all_num % x == 0:
                    return all_num % 1337
                x -= 1
            right_half_num -= 1
