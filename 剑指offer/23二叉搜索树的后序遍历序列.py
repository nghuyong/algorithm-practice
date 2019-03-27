#!/usr/bin/env python
# encoding: utf-8
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        """
        :param sequence: 输入序列
        :return: 判断是否是二叉搜索树的后序遍历
        """
        if not sequence:
            return False
        # 根节点
        root = sequence[-1]
        # 确定左子树序列
        index = 0
        while index < len(sequence) - 1:
            if sequence[index] > root:
                break
            index += 1
        # check 后面的数字均是大于root的
        for i in range(index, len(sequence) - 1):
            if sequence[i] < root:
                return False
        left = True
        if sequence[:index]:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if sequence[index:-1]:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right
