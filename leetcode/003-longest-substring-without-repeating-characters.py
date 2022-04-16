#!/usr/bin/env python
# encoding: utf-8
"""
File Description: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
Author: rightyonghu
Created Time: 2022/4/16
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window_set = set()
        max_window_len = 0
        while right < len(s):
            if s[right] in window_set:
                for i in range(left, right):
                    window_set.remove(s[i])
                    if s[i] == s[right]:
                        left = i + 1
                        break
            window_set.add(s[right])
            window_len = (right - left + 1)
            max_window_len = max(max_window_len, window_len)
            right += 1
        return max_window_len
