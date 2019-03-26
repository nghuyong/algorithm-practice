#!/usr/bin/env python
# encoding: utf-8
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, node):
        self.stack.append(node)
        if not self.assist:
            self.assist.append(node)
        else:
            current_min = self.min()
            if node < current_min:
                self.assist.append(node)
            else:
                self.assist.append(current_min)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.assist.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.assist[-1]
