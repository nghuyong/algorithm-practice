#!/usr/bin/env python
# encoding: utf-8
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class Solution:
    def PrintFromTopToBottom(self, root):
        """
        :param root: 二叉树的根节点
        :return: 打印序列
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            children = []
            for node in stack:
                result.append(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            stack = children
        return result
