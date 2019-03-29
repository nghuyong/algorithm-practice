#!/usr/bin/env python
# encoding: utf-8
"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


class Solution:
    def PrintMinNumber(self, numbers):
        """
        :param numbers: 输入数组
        :return: 拼接起来最小的数字
        """
        if not numbers:
            return ""

        def compare(x, y):
            x_str = str(x)
            y_str = str(y)
            max_len = max(len(x_str), len(y_str))
            x_str = x_str + x_str[-1] * (max_len - len(x_str))
            y_str = y_str + y_str[-1] * (max_len - len(y_str))
            if x_str < y_str:
                return -1
            elif x_str > y_str:
                return 1
            else:
                return 0

        numbers.sort(cmp=compare)

        return "".join(map(str, numbers))


if __name__ == '__main__':
    print(Solution().PrintMinNumber([3, 32, 321]))
