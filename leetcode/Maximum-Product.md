---
title: Leetcode-Maximum Product of Three Numbers
date: 2017-11-01 15:30:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)
```
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

```
<!--more-->

# 分析
一开始不知道有负数存在的情况，所以就很简单，找到最大的三个数就可以了。不需要排序，可以在O(n)内找到。

后来提交的时候意识到会存在负数的情况！！

所以就是**找出最大的三个数和最小的两个数**。这个是一定存在的，这里面不需要考虑正负，就是**不是找出最大的三个正数和最小的两个负数**，这个就不一定存在了！！！

一开始给这个错误的想法给误导了！！！！

具体编码的时候，最大的数，一开始赋初值为最小的值，最小的数，一开始赋初值位最大的值！！！

**不需要用题设中的数来作为初值的！！**

# AC代码
```C++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int min1,min2,max1,max2,max3;
        min1 = min2 = 1000;
        max1 = max2 = max3 = -1000;
        for(auto num : nums){
            //另外一种比较顺序会更简洁！！
            if(num>max3){
                if(num>max2){
                    if(num>max1){
                        max3 = max2;
                        max2 = max1;
                        max1 = num;
                    }else{
                       max3 = max2;
                        max2 = num;
                    }
                }else{
                    max3 = num;
                }
            }
            
            if(num<min2){
                if(num<min1){
                    min2 = min1;
                    min1 = num;
                }else{
                    min2 = num;
                }
            }
        }
        return max(max1*max2*max3 , min1*min2*max1);
    }
};
```