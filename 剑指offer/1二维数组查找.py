#!/usr/bin/env python
# encoding: utf-8
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def find(target, array):
    """
    :param target: 查找的目标数字
    :param array: 待查找的数组
    :return: True/False
    """
    if not array:
        return None
    rows = len(array)
    cols = len(array[0])
    x, y = 0, cols - 1
    while 0 <= x < rows and 0 <= y < cols:
        cur_val = array[x][y]
        if cur_val == target:
            return True
        elif cur_val < target:
            y -= 1
        else:
            x += 1
    return False
