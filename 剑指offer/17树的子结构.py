#!/usr/bin/env python
# encoding: utf-8
"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        """
        :param pRoot1: 第一棵树
        :param pRoot2: 第二棵树
        :return: 第二棵树是不是第一棵树的子结构
        """
        if not pRoot2:
            return False
        if not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            if self.check_is_subtree(pRoot1, pRoot2):
                return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def check_is_subtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.check_is_subtree(pRoot1.left, pRoot2.left) and self.check_is_subtree(pRoot1.right, pRoot2.right)
