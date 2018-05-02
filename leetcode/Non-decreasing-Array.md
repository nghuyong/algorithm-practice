---
title: Leetcode-Non-decreasing Array
date: 2017-11-06 21:40:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/description/)
```
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 
4
 to 
1
 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].

```
<!--more-->

# 分析
这题，主要是寻找到分界线！！

在分界线就会有两种情况：

1. 3，5，4， 这种就要把5，改成4 或者 把5改成3
2. 3，5，2   这种只能把2，改成5

核心其实是，遇到**需要修改的，先改了**。这样后续，就能继续进行这样的判断和修改。

# AC代码
```C++
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int cnt = 0;                                                                    //the number of changes
        for(int i = 1; i < nums.size() && cnt<=1 ; i++){
            if(nums[i-1] > nums[i]){
                cnt++;
                if(i-2<0 || nums[i-2] <= nums[i])nums[i-1] = nums[i];                    //modify nums[i-1] of a priority
                else nums[i] = nums[i-1];                                                //have to modify nums[i]
            }
        }
        return cnt<=1;
    }
};
```