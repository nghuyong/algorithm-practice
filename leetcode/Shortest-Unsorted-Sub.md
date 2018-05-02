---
title: Leetcode-Shortest Unsorted Continuous Subarray
date: 2017-11-06 21:40:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/)
```
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

```
<!--more-->

# 分析
寻找中间乱序的部分。

一开始比较简单粗暴，再构建一个数组，然后排序，再把这个排好序的数组跟原来的数组的进行比较，从而找到乱序的部分，这种算法的复杂度为O(NlogN).

还有一种思路就是建立两个数组，分别为至今最大的，和至今最小的，分别从数组两端扫描。如果是有序的，那么当前的值就是该是从右向左看最小的，和总左往右看最大的。这种算法的复杂度为O(logN).

# AC代码
## O(NlogN)
```C++
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(),sortedNums.end());
        int length = nums.size();
        int start,end;
        for(start=0;start<length;start++){
            if(nums[start]!=sortedNums[start]){
                break;
            }
        }
        if(start==length)
            return 0;
        for(end=length-1;end>=0;end--){
            if(nums[end]!=sortedNums[end]){
                break;
            }
        }
        return end-start+1;
    }
};
```

## O(logN)
```C++
/**
 *            /------------\
 * nums:  [2, 6, 4, 8, 10, 9, 15]
 * minr:   2  4  4  8   9  9  15
 *         <--------------------
 * maxl:   2  6  6  8  10 10  15
 *         -------------------->
 */
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> maxlhs(n);   // max number from left to cur
        vector<int> minrhs(n);   // min number from right to cur
        for (int i = n - 1, minr = INT_MAX; i >= 0; i--) minrhs[i] = minr = min(minr, nums[i]);
        for (int i = 0,     maxl = INT_MIN; i < n;  i++) maxlhs[i] = maxl = max(maxl, nums[i]);

        int i = 0, j = n - 1;
        while (i < n && nums[i] <= minrhs[i]) i++;
        while (j > i && nums[j] >= maxlhs[j]) j--;

        return j + 1 - i;
    }
};
```