---
title: Leetcode-Set Matrix Zeroes
date: 2017-11-15 19:43:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)
```
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
```
<!--more-->

# 分析
这是咋看起来很简单，就是把0的横竖都置成0，但是其核心是在线处理！

不能使用多余的空间。

一开始的思路，还是一个标记，就是对存在0的横行和竖列都进行标记，最后还能恢复成0.

一开始想用最大整数／最小整数进行标记，但是测试用例中，就存在这样的用例！

所以，一直不能AC。

后来，看了discuss，是对第一行和第一列进行标记实现的。而对于第一列的情况，还需要单独处理一下。

值得注意的是，最后进行恢复为0的时候，需要从最后一排，最后一列开始，倒过来恢复。

## AC代码
```C++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int col0 = 1;
        for(int i=0;i<m;i++){
            if(matrix[i][0] == 0) 
                col0 = 0;
            for(int j=1;j<n;j++){
                if(matrix[i][j]==0){
                    matrix[0][j] = matrix[i][0] = 0;
                }
            }
        }
        
        for(int i=m-1;i>=0;i--){
            for(int j=n-1;j>=1;j--){
                if(matrix[i][0]==0 || matrix[0][j]==0)
                    matrix[i][j] = 0;
            }
            if(col0==0)
                matrix[i][0] = 0;
        }
        
    }
};
```