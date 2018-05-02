---
title: Leetcode-Contains Duplicate II
date: 2017-11-06 21:12:02
categories: Leetcode
tags: 
 - Hash
 - Array
---

# 题目描述
[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/)
```
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
```
<!--more-->

# 分析
这题一开始还没理解题目的意思，其实就是在数组中，寻找两个相同的数，如果之间距离小于或者等于K，就返回True，否则就返回False。

一开始想到的就是用map来做，记录数组中每个值的位置信息，但是，一开始处理重复出现的值，是采用一个vector来挨个记录。实际上，**可以直接覆盖！**

因为，只需要保留距离游标最近的值的坐标就可以了。如果这个都不能满足小于等于k，前面的那些值肯定也是不满足的。

# AC代码
```C++
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> hash_map;
        int length = nums.size();
        for(int i=0;i<length;i++){
            if (hash_map.find(nums[i])!=hash_map.end()){
                if(i-hash_map[nums[i]]<=k)
                    return true;
            }
                
            hash_map[nums[i]] = i;
        }
        return false;
        
    }
};
```