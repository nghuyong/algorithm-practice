---
title: Leetcode-Rotate Image
date: 2017-11-13 20:49:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Rotate Image](https://leetcode.com/problems/rotate-image/description/)
```
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

```
<!--more-->

# 分析
这题我采用了一个折中的方案，一圈一圈的进行旋转。

主要核心就是不使用额外的空间！

看了Discuss发现了一种很神奇的旋转90度的方法。

对于顺时针就是，先上下颠倒，然后再对称得进行交换

而逆时针旋转，就是先左右颠倒，然后再对称得进行交换


## AC代码
我的方案，一圈一圈的旋转
```C++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int half_n = n/2;
        for(int row = 0,R = n;row<half_n;row++,R-=2){
            changeOneCircle(matrix,R,row,n);
        }
        
    }
    
    void changeOneCircle(vector<vector<int>>& matrix,int R,int row,int n){
        int up,right,down,left,col;
        for(int i=0;i<R-1;i++){
            col = row + i;
            
            up = matrix[row][col];
            right = matrix[col][n-1-row];
            down = matrix[n-1-row][n-1-col];
            left = matrix[n-1-col][row];
            
            matrix[row][col] = left;
            matrix[col][n-1-row] = up;
            matrix[n-1-row][n-1-col] = right;
            matrix[n-1-col][row] = down;
        }
    }
};
```

更优雅的方案
```C++
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}
```