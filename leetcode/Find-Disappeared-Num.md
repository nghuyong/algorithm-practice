---
title: Leetcode-Find All Numbers Disappeared in an Array
date: 2017-11-01 13:12:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Find All Numbers Disappeared in an Arra](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)
```
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
<!--more-->

# 分析
本题的关键是不使用额外的空间，还需要是在O(n)的时间范围内完成操作。

所以，必须思考，怎么样在数字的编号上进行标记，但是不会改变这个位置上数据的值。

数据以Input数据为例，a[0] = 4，表明4已经出现过了，需要标记一下。但是又不能新开一个数组在`mark[4] = true`,所以这就需要在原数组上做文章。

可以有两种方法：

1. 令 `a[3] = a[3]+N` 这样`a[3]`位置上的值虽然改变了，但是通过`a[3]%N`这个操作一定可以恢复出`a[3]`原来的值，因为`0<=a[i]<N`.这样数据被标记为小于N的数，和大于等于N的数据。显然，大于等于N的数的编号就是没有出现过的。

2. 令`a[3] = -a[3]`,通过`abs(a[3])`可以恢复出原值。这样数据被标记为正数和负数。显然，正数的编号就是没有出现过的。



# AC代码
方案一：
```C++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> result;
        for(int i=0;i<n;i++){
            nums[(nums[i]-1)%n] += n;
        }
        for(int i=0;i<n;i++){
            if(nums[i]<=n)
                result.push_back(i+1);
        }
        return result;
    }
};
```

方案二：
```C++
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int len = nums.size();
        for(int i=0; i<len; i++) {
            int m = abs(nums[i])-1; // index start from 0
            nums[m] = nums[m]>0 ? -nums[m] : nums[m];
        }
        vector<int> res;
        for(int i = 0; i<len; i++) {
            if(nums[i] > 0) res.push_back(i+1);
        }
        return res;
    }
};
```

类似的问题：
[Submission Details](https://leetcode.com/submissions/detail/128150122/)