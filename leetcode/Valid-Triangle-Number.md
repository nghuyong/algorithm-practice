---
title: Leetcode-Valid Triangle Number
date: 2017-11-09 19:54:02
categories: Leetcode
tags: 
 - 二分查找
 - Array
---

# 题目描述
[Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/description/)
```
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
```
<!--more-->

# 分析
这题是寻找能够成三角形的三个数。

一开始第一印象是深度搜索。。。

后来发现还是自己想复杂了，深搜是肯定超时的，一定要剪枝。

也就是三角形，短的两边之和大于第三边，那么固定了前两个短的边，对于第三条边，只要依次遍历直到不符合条件，由于数组是按顺序排放的，所以后面的数据，肯定也是不符合条件的。

一旦看到这个剪枝，就能发现，其实可以直接通过二分，找到那个第一个不能构成三角形的数。

## AC代码
### DFS
```C++
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        vector<int> path;
        int count = 0;
        sort(nums.begin(),nums.end());
        dfs(path,&count,nums,0);
        return count;
    }
    
    
    void dfs(vector<int>& path,int *count,vector<int>& nums,int current ){
        if(path.size()==3){
            (*count) ++;
            return;
        }
        for(int i=current;i<nums.size();i++){
            if(path.size()==2 && nums[i]>=path[0]+path[1]){
                break;
            }
            path.push_back(nums[i]);
            dfs(path,count,nums,i+1);
            path.pop_back();
        }
    }
};
```
### 二分查找
```C++
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int count = 0;
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int maxOne = findTheMax(j+1,nums[i]+nums[j],nums);
                count += (maxOne-j);
            }
        }
        return count;
    }
    
    int findTheMax(int start,int target,vector<int>& nums){
        int low = start;
        int high = nums.size()-1;
        while(low<=high){
            int middle = (low+high)/2;
            if(nums[middle]<target)
                low = middle+1;
            else
                high = middle-1;
        }
        return high;
    }
};
```