#!/usr/bin/env python
# encoding: utf-8
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """
        :param rotateArray: 输入旋转的数组
        :return: 旋转数组最小的元素
        """
        if not rotateArray:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        left = 0
        right = len(rotateArray) - 1
        while right - left > 1:
            mid = (left + right) // 2
            if rotateArray[mid] >= rotateArray[0]:
                left = mid
            elif rotateArray[mid] <= rotateArray[len(rotateArray) - 1]:
                right = mid
        # 假设只有两个数字的场景是不好判断的
        return min(rotateArray[left], rotateArray[right])
