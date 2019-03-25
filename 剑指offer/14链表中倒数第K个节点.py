#!/usr/bin/env python
# encoding: utf-8
"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        """
        :param head: 链表的头指针
        :param k: 数字K
        :return: 倒数K个节点
        """
        if not head:
            return None
        if k < 1:
            return None
        left, right = head, head
        for i in range(k):
            if not right:
                return None
            right = right.next
        while right:
            right = right.next
            left = left.next
        return left
