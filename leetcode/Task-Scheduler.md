---
title: Leetcode-Task Scheduler
date: 2017-11-08 20:08:02
categories: Leetcode
tags: 
 - 优先队列
 - Array
---

# 题目描述
[Task Scheduler](https://leetcode.com/problems/task-scheduler/description/)
```
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

```
<!--more-->

# 分析
这题一开始还真没什么好的思路

其实并不是简单的按照FIFO进行任务调度，就能实现时间最短

需要按照任务多的先调度，所以结构上就要采用一个优先队列来处理。

还有一个很关键的就是实际上是存在一个周期，每个周期其实都是彼此独立的，而且每隔周期内，任务不可重复。

# AC代码
```C++
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char,int> counts;
        for(char t:tasks){
            counts[t]++;
        }
        priority_queue<int> pq;
        for(pair<char,int>count:counts){
            pq.push(count.second);
        }
        int alltime = 0;
        int cycle = n+1;
        while(!pq.empty()){
            int time = 0;
            vector<int> tmp;
            for(int i=0;i<cycle;i++){
                if(!pq.empty()){
                    tmp.push_back(pq.top());
                    pq.pop();
                    time++;
                }
            }
                for(int cnt:tmp){
                    if(--cnt){
                        pq.push(cnt);
                    }
                }
                
                if(!pq.empty()){
                    alltime += cycle;
                }else{
                    alltime += time;
                }                
            }
        return alltime;
    }
};
```