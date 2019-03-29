#!/usr/bin/env python
# encoding: utf-8
"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


class Solution:

    def GetUglyNumber_Solution(self, index):
        """
        :param index: 第index个
        :return:
        """
        if index < 7:
            return index
        res = [1]
        t2, t3, t5 = 0, 0, 0
        while len(res) < index:
            res.append(min(res[t2] * 2, res[t3] * 3, res[t5] * 5))
            if res[-1] == res[t2] * 2:
                t2 += 1
            if res[-1] == res[t3] * 3:
                t3 += 1
            if res[-1] == res[t5] * 5:
                t5 += 1
            # print(res)
        return res[-1]


if __name__ == '__main__':
    Solution().GetUglyNumber_Solution(7)
