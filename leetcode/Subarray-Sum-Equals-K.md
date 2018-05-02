---
title: Leetcode-Subarray Sum Equals K
date: 2017-11-09 20:09:02
categories: Leetcode
tags: 
 - Hash
 - Array
---

# 题目描述
[Subarray Sum Equals K](https://leetcode.com/submissions/detail/127469475/)
```
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

```
<!--more-->

# 分析
题意就是寻找一段连续的子数组，加和为给定的数。

我一开始用了一个很垃圾的方法，强行AC了。

其实核心就是计算所有的A[i,j]当然，可以做一点优化。

```
we know the key to solve this problem is SUM[i, j]. So if we know SUM[0, i - 1] and SUM[0, j], then we can easily get SUM[i, j]. To achieve this, we just need to go through the array, calculate the current sum and save number of all seen PreSum to a HashMap. Time complexity O(n), Space complexity O(n).
```

所以核心就是通过Set来存储这些SUM[0,i],这样得到了SUM[0,j]，只需寻找是否存在SUM[0,j]-k，如果存在SUM[0,i-1] == SUM[0,j]-k , 那么 SUM[i,j] = k

## AC代码
```C++
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int cum=0; // cumulated sum
        map<int,int> rec; // prefix sum recorder
        int cnt = 0; // number of found subarray
        rec[0]++; // to take into account those subarrays that begin with index 0
        for(int i=0;i<nums.size();i++){
            cum += nums[i];
            cnt += rec[cum-k];
            rec[cum]++;
        }
        return cnt;
    }
};
```