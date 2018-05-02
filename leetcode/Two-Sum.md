---
title: Leetcode-Two Sum
date: 2017-11-04 13:04:02
categories: Leetcode
tags: 
 - Hash
 - Array
---

# 题目描述
[Two Sum](https://leetcode.com/problems/two-sum/description/)
```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
<!--more-->

# 分析
这是一道很典型的hash题，通过hash映射[值]和[编号]

一开始有点僵化了，先hash映射，再排序，就转化成了原先做过的一道题[Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/),在一个有序的数组中寻找两个数相加等于给定值。

后来意识到，这里已经使用了hashmap，寻找下一个值会非常方便，完全不需要再排序！！

## AC代码
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> dic;
        int length = nums.size();
        for(int i=0;i<length;i++){
            if(dic.find(target-nums[i])==dic.end()){
                dic[nums[i]] = i;
            }else{
                return {i,dic[target-nums[i]]};
            }
        }
    }
};
```