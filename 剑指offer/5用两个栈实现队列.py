#!/usr/bin/env python
# encoding: utf-8
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, node):
        self.stack_in.append(node)

    def pop(self):
        # 如果stack_out已经有元素，就直接弹出元素
        if self.stack_out:
            return self.stack_out.pop()
        else:
            # 没有需要将stack_in中的元素依次压入stack_out中
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.pop()
