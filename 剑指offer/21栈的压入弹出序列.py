#!/usr/bin/env python
# encoding: utf-8
"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        """
        :param pushV: 压入序列
        :param popV: 弹出序列
        :return: 弹出序列是否正常
        """
        stack = []
        pop_index = 0
        for item in pushV:
            stack.append(item)
            while stack and pop_index < len(popV) and stack[-1] == popV[pop_index]:
                stack.pop()
                pop_index += 1
        return len(stack) == 0
