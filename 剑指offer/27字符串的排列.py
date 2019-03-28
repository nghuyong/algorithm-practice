#!/usr/bin/env python
# encoding: utf-8
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution:
    def __init__(self):
        self.path = []
        self.result = set()

    def Permutation(self, ss):
        if not ss:
            return self.path
        self.dfs(ss)
        return sorted(list(self.result))

    def dfs(self, ss):
        if len(self.path) == len(ss):
            self.result.add("".join([ss[index] for index in self.path]))
            return
        for i in range(len(ss)):
            if i not in self.path:
                self.path.append(i)
                self.dfs(ss)
                self.path.pop()
