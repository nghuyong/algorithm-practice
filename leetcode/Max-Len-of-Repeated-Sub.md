---
title: Leetcode-Maximum Length of Repeated Subarray
date: 2017-11-10 20:06:02
categories: Leetcode
tags: 
 - DP
 - Array
---

# 题目描述
[Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/)
```
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
```
<!--more-->

# 分析
这题一开始没什么好的思路，就暴力求解，当然是超时的。

后来看了discuss，才发现这是一道DP的题目。

就是DP[i][j]表示，以A[i],B[j]结尾的，最大重复字串个数。

那么如果A[i]=B[j],DP[i][j]=DP[i-1][j-1]+1

## AC代码
```C++
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int max_count = 0;
        vector<vector<int>> dp(A.size()+1,vector<int>(B.size()+1,0));
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                if (A[i] == B[j]) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                    max_count = max(max_count, dp[i + 1][j + 1]);
                }
            }
        }
        return max_count;
    }
};
```