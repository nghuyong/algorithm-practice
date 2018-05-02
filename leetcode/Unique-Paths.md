---
title: Leetcode-Unique Paths
date: 2017-11-09 19:55:02
categories: Leetcode
tags: 
 - DP
 - Array
---

# 题目描述
[Unique Paths](https://leetcode.com/problems/unique-paths/description/)
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
```

![](https://leetcode.com/static/images/problemset/robot_maze.png)
<!--more-->

# 分析
一开始一位就是一道简单的走迷宫，那种题目，所以直接就是DFS了。

这种方案就是超时的。

后来一想，这就是一道DP！因为只能向右和向下走，所以，

`DP[i][j] = DP[i-1][j] + DP[i][j-1]`

## AC代码
```C++
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> map(m+1,vector<int>(n+1,0));
        map[0][1] = 1;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                map[i][j] = map[i-1][j] + map[i][j-1];
            }
        }
        return map[m][n];
    }
};
```