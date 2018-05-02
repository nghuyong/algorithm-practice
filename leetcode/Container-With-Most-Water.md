---
title: Leetcode-Container With Most Water
date: 2017-11-15 19:37:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)
```
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
```
<!--more-->

# 分析
这题就是典型的短板原理。

核心就是要寻找到i,j，使得(j-i)*min(nums[i],nums[j)最大。

可以看到这里面有两个变量，如果按同一个方向进行遍历，肯定需要两层循环。

所以，可以固定使得，其中一个是递减的，这样，就可以在一层循环内完成。

那就是保持，j-i在不断减少，那么新的值要想比原来的值大，就只能是min(nums[i],nums[j])这个数，更大。

## AC代码
```C++
class Solution {
public:
    int maxArea(vector<int>& height) {
         int water = 0;
         int i = 0, j = height.size() - 1;
         while (i < j) {
            int h = min(height[i], height[j]);
            water = max(water, (j - i) * h);
            while (height[i] <= h && i < j) i++;
            while (height[j] <= h && i < j) j--;
        }
        return water;
    }
};
```