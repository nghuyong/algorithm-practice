#!/usr/bin/env python
# encoding: utf-8
"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


class Solution:

    def NumberOf1Between1AndN_Solution(self, n):
        """
        :param n: 终止数字n
        :return: 1出现的次数
        """
        if n <= 0:
            return 0
        count = 0
        base = 1
        while base <= n:
            deliver = base * 10
            count += (n // deliver) * base + min(max(n % deliver - base + 1, 0), base)
            base *= 10
        return count
