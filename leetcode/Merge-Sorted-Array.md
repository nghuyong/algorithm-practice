---
title: Leetcode-Merge Sorted Array
date: 2017-11-06 21:20:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)
```
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
```
<!--more-->

# 分析
这就是很经典的归并排序算法！

但是有要求的，就是只使用给定的两个数组，将第二个数组Merge到第一个数组里面，不能创建第三个结果数组。

所以，一开始智障了，不知道怎么仅仅用两个数组就能完成，难道不会覆盖第一个数组的数据吗？？？

后来恍然，原来是**倒着Merge，因为第一个数组后面都是空的**！

这得记录下来！

# AC代码
```C++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1;
        int j = n-1;
        int k = m+n-1;
        while(j>=0 && i>=0){
            if(nums1[i]>=nums2[j]){
                nums1[k--] = nums1[i--];
            }else{
                nums1[k--] = nums2[j--];
            }
        }
        while(j>=0)
            nums1[k--] = nums2[j--];
    }
};
```