---
title: Leetcode-Contains Duplicate
date: 2017-11-01 14:58:02
categories: Leetcode
tags: 
 - Hash
 - Array
---

# 题目描述
[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)
```
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
```
<!--more-->

# 分析
这题的核心其实是**检验重复**，根据常识，最好的去重复方法就是set了。所以只要验证set内的元素个数与原来的数组重的元素个数是否相同即可。

# AC代码
```C++
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        int length = nums.size();
        for(int i=0;i<length;i++){
            s.insert(nums[i]);
        }
        return s.size() < length;
        
    }
};
```