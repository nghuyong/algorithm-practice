#!/usr/bin/env python
# encoding: utf-8
"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        """
        :param pRootOfTree: 二叉搜索树的根节点
        :return: 节点的指针
        """
        return self.ConvertV2(pRootOfTree)[0]

    def ConvertV2(self, pRootOfTree):
        if not pRootOfTree:
            return None, None
        root_node = pRootOfTree
        left_tree_head, left_tree_tail = self.ConvertV2(pRootOfTree.left)
        right_tree_head, right_tree_tail = self.ConvertV2(pRootOfTree.right)
        if left_tree_tail:
            root_node.left = left_tree_tail
            left_tree_tail.right = root_node
        if right_tree_head:
            right_tree_head.left = root_node
            root_node.right = right_tree_head
        final_left_head = left_tree_head if left_tree_head else root_node
        final_right_tail = right_tree_tail if right_tree_tail else root_node
        return final_left_head, final_right_tail
