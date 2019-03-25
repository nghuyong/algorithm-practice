#!/usr/bin/env python
# encoding: utf-8
"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        """
        :param pHead: 原来链表的头节点
        :return: 反转后链表的头节点
        """
        # 0个节点
        if not pHead:
            return pHead
        # 1个节点
        if not pHead.next:
            return pHead
        before_node = None
        cur_node = pHead
        while cur_node:
            next_node = cur_node.next
            cur_node.next = before_node
            before_node = cur_node
            cur_node = next_node
        return before_node
