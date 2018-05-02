---
title: Leetcode-Product of Array Except Self
date: 2017-11-08 20:09:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
```
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
```
<!--more-->

# 分析
要求计算除了自己本身之外其他数字的乘积，而且不能使用除法。

一直就没有什么好的思路。

看了讨论之后恍然大悟，原来有一种非常优雅的方案：

就是两个游标，一个一直计算到这个数左边所有数的乘积，另外一个一直计算到这个数右边所有数的乘积。然后两者相乘就是结果了。

# AC代码
```C++
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> result(nums.size(),1);
        
        int left = 1;
        for(int i=0;i<length;i++){
            result[i] *= left;
            left *= nums[i];
        }
        
        
        int right = 1;
        for(int i=length-1;i>=0;i--){
            result[i] *= right;
            right *= nums[i];
        }
        
        return result;
        
    }
};
```