---
title: Leetcode-Search Insert Position
date: 2017-10-29 13:50:02
categories: Leetcode
tags: 
 - 二分查找
 - Array
---

# 题目描述
[Search Insert Position](https://leetcode.com/problems/search-insert-position/description/)
```
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
```
<!--more-->
# 分析
简单的说：给定一个数组(有序)和一个数字。如果数字在数组中存在返回所在的位置，如果不存在，返回应该插入的位置。

显然这是二分查找的题目，但是具体要分析一下，如果数据不存在，**返回的待插入位置什么？**

1)二分查找的循环条件为 low<=high ，如果跳出的循环，说明**没有找到，而且low>high 也就是low>=high+1**

2)又有一个不变的条件，**返回的待插入位置一定在[low,high+1]之间，也就是low<=high+1**

结合1),2)，一旦跳出循环，**low=high+1,待插入的位置在[low,low]之间，所以，也就是low。**

# AC代码
```C++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int high = nums.size()-1,low = 0;
        while(low<=high){
            int middle = (low+high)/2;
            if (nums[middle]==target){
                return middle;
            }
            else if (nums[middle]<target){
                low = middle+1;
            }else{
                high = middle-1;
            }
        }
        return low;
    }
};
```

