#!/usr/bin/env python
# encoding: utf-8
"""
输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        """
        :param pHead: 原节点的头部
        :return: 克隆后的头节点
        """
        # 先在每个节点后面插入一个节点
        if not pHead:
            return None
        p = pHead
        while p:
            p_next = p.next
            new_node = RandomListNode(p.label)
            p.next = new_node
            new_node.next = p_next
            p = p_next
        # 设置random
        p = pHead
        while p:
            p_cloned = p.next
            p_random = p.random
            if p_random:
                p_cloned.random = p_random.next
            p = p_cloned.next
        # 分离
        cloned_head = pHead.next
        p = pHead
        while p.next:
            temp = p.next
            p.next = temp.next
            p = temp
        return cloned_head
