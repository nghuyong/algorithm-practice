---
title: Leetcode-Degree of an Array
date: 2017-11-01 13:32:02
categories: Leetcode
tags: 
 - Array
 - Hash
---

# 题目描述
[Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/)
```
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
```

<!--more-->

# 分析
这题一直没什么好的思路，直到看了discuss才有点明白。

核心是要记录下，相同数字在数组中的起始位置，结束位置，和出现的次数。

最后就可以很方便的找到出现次数最多，长度又最小的子串。

之所以可以这么做，是因为这里面**子串一定是连续的**，所以只用记录首尾就够了。

具体实现，用到了`unordered_map`这个数据结构，这是一个无顺序的`map`。

# AC代码
```C++
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int length = nums.size();
        unordered_map<int ,int> start;
        unordered_map<int ,int> end;
        unordered_map<int ,int> count;
        int max_count = 0;
        for(int i=0;i<length;i++){
            if(start.find(nums[i]) == start.end() ){
                //没找到
                start[nums[i]] = i;
                count[nums[i]] = 1;
            }else{
                end[nums[i]] = i;
                count[nums[i]]++;
                
            }
            end[nums[i]] = i;
            max_count = max(max_count , count[nums[i]]);
        }
        unordered_map<int,int>::iterator it;
        int min_len = 49999;
        for(it=count.begin();it!=count.end();it++){
            if(it->second!=max_count)
                continue;
            min_len = min( (end[it->first] - start[it->first] +1) , min_len);
        }
        return min_len;
    }
};
```