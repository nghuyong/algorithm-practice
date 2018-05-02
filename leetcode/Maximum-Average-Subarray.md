---
title: Leetcode-Maximum Average Subarray
date: 2017-11-04 13:36:02
categories: Leetcode
tags: 
 - SlideWindow
 - Array
---

# 题目描述
[Maximum Average Subarray](https://leetcode.com/problems/maximum-average-subarray-i/description/)
```
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

```
<!--more-->

# 分析
这题一开始确实没什么好的思路。

就开始简化，假设k为1，那就是寻找这个数组的最大值啊。

那么就是一层循环，里面逐个比较。

```C++
for(int i=0;i+k<=length;i++){
    int tmp_sum = 0;
    for(int j=0;j<k;j++){
        tmp_sum += nums[i+j];
    }
    max_sum = max(tmp_sum,max_sum);
}
```

但是提交以后就是超时的。这个算法是O(n*k)

后来观察了一下没有过的通过用例，K非常大，有5000多。那么我每次计算其实是重复的。

也就是前一个窗口计算:

```C++
tmp_sum = nums[i-1]+nums[i]+nums[i+1]+....nums[i+k-2]
```

当前窗口的计算：

```
new_tmp_sum = nums[i]+nums[i+1]+....+nums[i+k-1]
```

可以发现，中间部分完全相同，所以下一个窗口不用重新计算，只需要在上一个窗口计算的结果上加以修正。

new_tmp_sum = tmp_sum -nums[i-1]+nums[i+k-1]

这样变成了一个O(n)的算法

# AC代码
```C++
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int length = nums.size();
        int current_tmp_sum = 0;
        int last_tmp_sum = 0;
        for(int j=0;j<k;j++)
            last_tmp_sum += nums[j];
        int max_sum = last_tmp_sum;
        for(int i=1;i+k<=length;i++){
            current_tmp_sum = last_tmp_sum - nums[i-1] + nums[i+k-1];
            last_tmp_sum = current_tmp_sum;
            max_sum = max(max_sum,current_tmp_sum);
        }
        return max_sum*1.0/k;
    }
};
```