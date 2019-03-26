#!/usr/bin/env python
# encoding: utf-8
"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def printMatrix(self, matrix):
        """
        :param matrix: 输入矩阵
        :return: 顺序打印的列表
        """
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        x_start = 0
        y_start = 0
        while rows >= 1 and cols >= 1:
            x_end = x_start + rows - 1
            y_end = y_start + cols - 1
            if rows == 1:
                for i in range(y_start, y_end + 1):
                    result.append(matrix[x_start][i])
                break
            if cols == 1:
                for i in range(x_start, x_end + 1):
                    result.append(matrix[i][y_start])
                break
            # ->
            for i in range(y_start, y_end):
                result.append(matrix[x_start][i])
            # |
            for i in range(x_start, x_end):
                result.append(matrix[i][y_end])
            # <-
            for i in range(y_start + 1, y_end + 1)[::-1]:
                result.append(matrix[x_end][i])
            # |
            for i in range(x_start + 1, x_end + 1)[::-1]:
                result.append(matrix[i][y_start])
            rows -= 2
            cols -= 2
            x_start += 1
            y_start += 1
        return result
