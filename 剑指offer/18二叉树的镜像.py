#!/usr/bin/env python
# encoding: utf-8
"""
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：
源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, root):
        """
        :param root: 源二叉树
        :return: 镜像二叉树的根节点
        """
        if not root:
            return None
        mirrored_left = self.Mirror(root.left)
        mirrored_right = self.Mirror(root.right)
        root.left = mirrored_right
        root.right = mirrored_left
        return root
