---
title: Leetcode-Rotate Array
date: 2017-11-06 22:08:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Rotate Array](https://leetcode.com/problems/rotate-array/description/)
```
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

```
<!--more-->

# 分析
这里是将一个数组循环右移k的单位。

我采用的策略比较垃圾，是不断的移除最后一个元素然后插入到开头。

当然也可以编写一个右移一位的函数，然后循环执行k次，即可。

当然还有一种极其优雅的方式！！

就是先把前n-k的数做一次翻转，再把后面的k的数做一次翻转，最后再整体做一个翻转。

比如 1,2,3,4,5,6,7,8 循环右移3位
1. 前5个数翻转 5,4,3,2,1,6,7,8
2. 后3个数翻转 5,4,3,2,1,8,7,6
3. 整体翻转一次 6,7,8,1,2,3,4,5
可以看到成功完成了右移。


# AC代码
## O(NlogN)
```C++
class Solution 
    {
    public:
        void rotate(int nums[], int n, int k) 
        {
            k = k%n;
    
            // Reverse the first n - k numbers.
            // Index i (0 <= i < n - k) becomes n - k - i.
            reverse(nums, nums + n - k);
            
            // Reverse tha last k numbers.
            // Index n - k + i (0 <= i < k) becomes n - i.
            reverse(nums + n - k, nums + n);
            
            // Reverse all the numbers.
            // Index i (0 <= i < n - k) becomes n - (n - k - i) = i + k.
            // Index n - k + i (0 <= i < k) becomes n - (n - i) = i.
            reverse(nums, nums + n);
        }
    };
```

