#!/usr/bin/env python
# encoding: utf-8
"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, p):
        """
        :param p: 树的根节点
        :return:
        """
        return self.dfs(p) != -1

    def dfs(self, p):
        if p is None:
            return 0
        left = self.dfs(p.left)
        if left == -1:
            return -1
        right = self.dfs(p.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
