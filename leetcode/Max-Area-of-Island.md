---
title: Leetcode-Max Area of Island
date: 2017-10-30 23:12:02
categories: Leetcode
tags: 
 - BFS
 - DFS
 - Array
---

# 题目描述
[Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)
```
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
```

<!--more-->

# 分析
显然这是一道搜索题,DFS和BFS均可。

写代码的时候需要**注意细节！！！**

1. 在访问`map[i][j]`的时候一定要先检查`i`,`j`是否超出了范围，否则会报错！
2. BFS通过队列来实现，C++中q.pop()**不会返回值**,获得返回值需要通过q.front()

# AC代码
DFS
```C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int max_sum = 0;
        int row = grid.size();
        int col = grid[0].size();
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j]){
                    int sum = 0;
                    dfs(i,j,row,col,grid,&sum);
                    max_sum = max(max_sum,sum);
                }
            }
        }
        return max_sum;
    }
    
    
    void dfs(int i,int j, int row, int col, vector<vector<int>>& grid, int *sum){
        if (i<0||i>=row||j<0||j>=col||grid[i][j]==0){
            return ;
        }
        grid[i][j] = 0;
        *sum += 1;
        dfs(i+1,j,row,col,grid,sum);
        dfs(i-1,j,row,col,grid,sum);
        dfs(i,j+1,row,col,grid,sum);
        dfs(i,j-1,row,col,grid,sum);
    }
    
};
```

BFS
```C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();
        int next[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
        int max_count = 0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j]){
                    queue<int> q;
                    //也可以通过pair实现
                    q.push(i*col+j);
                    grid[i][j]=0;
                    int count = 1;
                    while(!q.empty()){
                        int index = q.front();
                        q.pop();
                        int current_i = index/col;
                        int current_j = index%col;
                        for(int next_index=0;next_index<4;next_index++){
                            int new_i = current_i+next[next_index][0];
                            int new_j = current_j+next[next_index][1];
                            if (new_i<0||new_j<0||new_i>=row||new_j>=col)
                                continue;
                            if(grid[new_i][new_j]){
                                q.push(new_i*col+new_j);
                                grid[new_i][new_j] = 0;
                                count++;
                            }
                            
                        }
                    }
                    max_count = max(max_count,count);
                }
            }
        }
        return max_count;
    }
};
```