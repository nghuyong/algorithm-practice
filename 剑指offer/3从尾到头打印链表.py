#!/usr/bin/env python
# encoding: utf-8
"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""


class Solution:
    def __init__(self):
        self.arrayList = []

    def printListFromTailToHead(self, listNode):
        """
        :param listNode: 链表的头指针 3->2->1
        :return:返回从尾部到头部的列表值序列，例如[1,2,3]
        """
        if not listNode:
            return self.arrayList
        self.printListFromTailToHead(listNode.next)
        self.arrayList.append(listNode.val)
        return self.arrayList
