#!/usr/bin/env python
# encoding: utf-8
"""
输入两个链表，找出它们的第一个公共结点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        :param pHead1: 第一个节点
        :param pHead2: 第二个节点
        :return: 第一个公共结点
        """

        def get_link_length(head):
            count = 0
            p = head
            while p:
                count += 1
                p = p.next
            return count

        def walk_n_step(head, n):
            p = head
            for i in range(n):
                p = p.next
            return p

        # 先确定两个链表的长度
        len1 = get_link_length(pHead1)
        len2 = get_link_length(pHead2)
        # 较长的链表先走
        if len1 > len2:
            pHead1 = walk_n_step(pHead1, len1 - len2)
        if len2 > len1:
            pHead2 = walk_n_step(pHead2, len2 - len1)
        # 再一起走
        p1, p2 = pHead1, pHead2
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
