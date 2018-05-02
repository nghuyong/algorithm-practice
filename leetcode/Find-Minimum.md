---
title: Leetcode-Find Minimum in Rotated Sorted Array
date: 2017-11-09 20:01:02
categories: Leetcode
tags: 
 - 二分查找
 - Array
---

# 题目描述
[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)
```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.


```
<!--more-->

# 分析
这题一开始没什么好的思路，就是寻找最下的数嘛。

简单的排序，输出第一个，竟然也AC了！而且，时间排名还很靠前！

后来看了讨论，才发现有更好的方案。

如果起点的数大于终点的数，就一定不存在旋转。否则，在通过二分，来进一步确定，旋转到底在那一段。

```
Classic binary search problem.

Looking at subarray with index [start,end]. We can find out that if the first member is less than the last member, there's no rotation in the array. So we could directly return the first element in this subarray.

If the first element is larger than the last one, then we compute the element in the middle, and compare it with the first element. If value of the element in the middle is larger than the first element, we know the rotation is at the second half of this array. Else, it is in the first half in the array.

Welcome to put your comments and suggestions.


```

## AC代码
```C++
class Solution {
public:
    int findMin(vector<int> &num) {
        int start=0,end=num.size()-1;
        
        while (start<end) {
            if (num[start]<num[end])
                return num[start];
            
            int mid = (start+end)/2;
            
            if (num[mid]>=num[start]) {
                start = mid+1;
            } else {
                end = mid;
            }
        }
        
        return num[start];
    }
};
```