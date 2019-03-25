#!/usr/bin/env python
# encoding: utf-8
"""
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""


class Solution:
    def Power(self, base, exponent):
        """
        :param base: 底数
        :param exponent: 指数
        :return: 底数 ^ 指数
        """
        p = abs(exponent)
        r = 1.0
        while p:
            if p & 1:
                r *= base
            base *= base
            p >>= 1
        return r if exponent >= 0 else 1.0 / r
