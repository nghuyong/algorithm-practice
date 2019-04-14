#!/usr/bin/env python
# encoding: utf-8
"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""


class Solution:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        # 对array中的数字进行异或运算
        tmp = 0
        for num in array:
            tmp ^= num
        # 获取tmp中最低位1的位置
        idx = 0
        """
        101
        001
        ---
        001
        """
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a = b = 0
        for num in array:
            if self.isBit(num, idx):
                a ^= num
            else:
                b ^= num
        return [a, b]

    def isBit(self, num, idx):
        """
        判断num的二进制从低到高idx位是不是1
        :param num: 数字
        :param idx: 二进制从低到高位置
        :return: num的idx位是否为1
        """
        num = num >> idx
        return num & 1
