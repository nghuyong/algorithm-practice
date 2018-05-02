---
title: Leetcode-Spiral Matrix II
date: 2017-11-10 20:13:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/description/)
```
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
<!--more-->

# 分析
这就是输出一个螺旋矩阵。

一开始的思路就是进行一个小模拟，按照螺旋的规则，依次填充。注意的是，就是要检查是否要改变填充的方向。

后来看了discuss，可以更直接的模拟填充。具体看代码了。。

## AC代码
我的方案
```C++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int next[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        vector<vector<int>> result(n,vector<int>(n,0));
        int direction=0,num=1,current_x=0,current_y=0;
        while(num<=n*n){
            result[current_x][current_y] = num++;
            if(checkDirection(current_x,current_y,direction,n,result,next)){
                direction++;
            }
            current_x = current_x + next[direction%4][0];
            current_y = current_y + next[direction%4][1];
        }
        return result;
    }
    
    bool checkDirection(int current_x,int current_y,int direction,int n,vector<vector<int>>& result,int next[4][2]){
        if(direction%4==0 && current_y==n-1)
            return true;
        if(direction%4==1 && current_x==n-1)
            return true;
        if(direction%4==2 && current_y==0)
            return true;
        int new_x = current_x + next[direction%4][0];
        int new_y = current_y + next[direction%4][1];
        if(result[new_x][new_y]!=0){
                return true;
        }
        return false;
    }
    
};
```

更直接的方案
```java
 public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
    
        int cur = 1;
        int rowBegin = 0;
        int rowEnd = n - 1;
        int colBegin = 0;
        int colEnd = n - 1;
        
        while(cur <= n * n) {
                //left to right
                for(j = colBegin ; j <= colEnd; j++){
                    res[rowBegin][j] = cur++;
                }
                rowBegin++;
                //top to bot
                for(i = rowBegin ; i <= rowEnd; i++){
                    res[i][colEnd] = cur++;
                }
                colEnd--;
                //right to left
                for(j = colEnd ; j >= colBegin; j--){
                    res[rowEnd][j] = cur++;
                }
                rowEnd--;
                //bot to top
                for(i = rowEnd; i >= rowBegin; i--){
                    res[i][colBegin] = cur++;
                }
                colBegin++;
        }
        return res;
    }
```