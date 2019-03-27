#!/usr/bin/env python
# encoding: utf-8
"""
输入一颗二叉树的跟节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def FindPath(self, root, expectNumber):
        """
        :param root: 二叉树根节点
        :param expectNumber: 整数
        :return:
        """
        if not root:
            return self.result
        self.dfs(root, expectNumber)
        return self.result

    def dfs(self, node, left_value):
        self.path.append(node.val)
        if not node.left and not node.right and left_value == node.val:
            self.result.append(self.path[::])
        left_value = left_value - node.val
        if node.left:
            self.dfs(node.left, left_value)
        if node.right:
            self.dfs(node.right, left_value)
        self.path.pop()