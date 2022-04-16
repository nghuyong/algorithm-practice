#!/usr/bin/env python
# encoding: utf-8
"""
File Description: https://leetcode-cn.com/problems/add-two-numbers/
Author: rightyonghu
Created Time: 2022/4/16
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = ListNode()
        p = pre_head
        carry = 0
        while l1 or l2:
            temp_sum = carry
            if l1:
                temp_sum += l1.val
            if l2:
                temp_sum += l2.val
            p.next = ListNode(temp_sum % 10)
            carry = temp_sum // 10
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            p.next = ListNode(carry)
        return pre_head.next
