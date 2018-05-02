---
title: Leetcode-Array Partition I
date: 2017-10-30 21:36:02
categories: Leetcode
tags: 
 - Hash
 - Array
---

# 题目描述
[Array Partition I](https://leetcode.com/problems/array-partition-i/description/)
```
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
```
<!--more-->

# 分析
这题简单的说，就是一个排序题！

现将给定的数组进行排序，然后从第一个数字开始，隔一个相加。

但是这个单纯的排序操作需要的时间规模至少是**O(nlgn)**

能不能优化呢？优化到**O(n)**,这就可以通过模拟hash来实现！

注意到之所以模拟hash是因为数据的范围是给定的！

具体来说，就是开辟一个20001的内存空间，初始空间的值为0，如果有值等于该空间的编号，则这个空间的值就加1.

由于空间的顺序是固定的，所以只要遍历空间，输出值不为0的空间的编号。（值为多少，就输出多少次）

## 举例说明
给一组范围在[0,9]的数组排序
```C++
int a[8] = {5,2,4,1,3,8,3,6};
int hash[10] = {0};
for(int i=0;i<8;i++){
    hash[a[i]]++;
}
for(int i=0;i<10;){
    if(hash[i]){
        printf("%d ",i);
        hash[i]--;
    }else{
        i++;
    }
}
```

# AC代码
```C++
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        //创建hash空间
        vector<short> hashtable(20001);
        for(auto e:nums){
            hashtable[e+10000]++;
        }
        int sum = 0;
        bool flag = true;
        for(int i=0;i<20001;){
            if(hashtable[i]>0){
                if(flag){
                    sum += (i-10000);
                    flag = false;
                }else{
                    flag = true;
                }
                hashtable[i]--;
            }else{
                i++;
            }
        }
        return sum;
    }
};
```