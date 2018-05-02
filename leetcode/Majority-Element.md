---
title: Majority Element
date: 2017-10-01 14:34:02
categories: Leetcode
tags: 
 - Array
 - Hash
---

# 题目描述
[Majority Element](https://leetcode.com/problems/majority-element/description/)
```
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
```
<!--more-->

# 分析
寻找一个数组中超过一半重复的数，而且一定存在这个数。

一开始做法很直接也很简单啊，统计每个数字出现的频率，最后遍历一下，找到超过一半的那个数字。

后来看到评论区发现了一个非常优雅的办法，设置一个count量，如果相同就++，如果不同就--，如果减到了0，就变成一个新的值，显然，最后超过一半的数字一定会胜出！！！

# AC代码
## Hashtable
```C++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts; 
        int n = nums.size();
        for (int i = 0; i < n; i++)
            if (++counts[nums[i]] > n / 2)
                return nums[i];
    }
};
```

## 优雅的做法
```C++
public class Solution {
    public int majorityElement(int[] num) {

        int major=num[0], count = 1;
        for(int i=1; i<num.length;i++){
            if(count==0){
                count++;
                major=num[i];
            }else if(major==num[i]){
                count++;
            }else count--;
            
        }
        return major;
    }
}
```