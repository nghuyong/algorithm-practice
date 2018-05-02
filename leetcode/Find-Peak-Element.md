---
title: Leetcode-Find Peak Element
date: 2017-11-14 19:32:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Find Peak Element](https://leetcode.com/problems/find-peak-element/description/)
```
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
```
<!--more-->

# 分析
这题要求在O(logn)时间内完成，所以就必须要通过二分查找来实现。
二分查找的关键，在于，能够二分的进行范围的缩小。
所以，就会有下面三种情况：
```
If num[i-1] < num[i] > num[i+1], then num[i] is peak
If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
If num[i-1] > num[i] < num[i+1], then both sides have peak
```
具体形成代码的时候需要注意边界的处理！

## AC代码
```C++
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;
        if(high==0)
            return 0;
        while(low<=high){
            int middle = (high+low)/2;
            if(middle==0){
                if(nums[middle]>nums[middle+1])
                    return middle;
                else
                    low = middle+1;
                continue;
            }
            if(middle==nums.size()-1){
                if(nums[middle]>nums[middle-1])
                    return middle;
                else
                    high = middle-1;
                continue;
            }
            if(nums[middle-1]<nums[middle] && nums[middle]>nums[middle+1]){
                return middle;
            }else if(nums[middle-1]<nums[middle] && nums[middle]<nums[middle+1]){
                low = middle+1;
            }else{
                high = middle-1;
            }
        }
        
    }
};
```