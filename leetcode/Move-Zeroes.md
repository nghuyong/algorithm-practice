---
title: Move Zeros
date: 2017-11-01 13:19:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Move Zeros](https://leetcode.com/problems/move-zeroes/description/)
```
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
```
<!--more-->

# 分析
这题显然也是要在线处理的，也就是不能在新开辟一个数组，非0就填充进去，最后再全部填充0.

一开始一直没什么好的思路，基本的想法是，顺序向后扫描，统计0的个数`zero_count`，如果遇到的数不是0，就向前移动`zero_count`个位置。最后再填充`zero_count`个0.

这种思路，最后也AC，但是感觉不是很纯粹。

更好的方案，也更纯粹一点的方案，就是再加一个游标`valid_index`如果遇到非0的数据，这个有效游标就向后移动1位。这就很完美的模拟出了最原始的新开辟一个数据的操作！！最后，再全部填充0.

# AC代码
我的渣渣想法
```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int length = nums.size();
        int zero_count = 0;
        for(int i=0;i<length;i++){
            if(nums[i]){
                nums[i-zero_count] = nums[i];
            }else{
                zero_count ++;
            }
        }
        for(int i=zero_count;i>0;i--){
            nums[length-i] = 0;
        }
    }
};
```

更纯粹的方案
```C++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j = 0;
        // move all the nonzero elements advance
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
        }
        for (;j < nums.size(); j++) {
            nums[j] = 0;
        }
    }
};
```