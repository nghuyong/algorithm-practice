#!/usr/bin/env python
# encoding: utf-8
"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        """
        :param pHead1: 第一个链表头指针
        :param pHead2: 第二个链表头指针
        :return: 合并以后链表的头指针
        """
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val > pHead2.val:
            pHead1, pHead2 = pHead2, pHead1
        final_head = pHead1
        p1, p2 = pHead1, pHead2
        # 将head2插入head1中
        while p1.next and p2:
            if p1.val <= p2.val <= p1.next.val:
                p1_next = p1.next
                p2_next = p2.next
                p1.next = p2
                p2.next = p1_next
                p2 = p2_next
            p1 = p1.next
        if p2:
            p1.next = p2
        return final_head
