---
title: Leetcode-Maximum Swap
date: 2017-11-13 19:00:02
categories: Leetcode
tags: 
 - DP
 - Array
---

# 题目描述
[Maximum Swap](https://leetcode.com/problems/maximum-swap/description/)
```
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]

```
<!--more-->

# 分析
这是一道DP问题，主要就是确保，从高位向地位扫描，一直都是最大的数字，如果不是，就把他和最大的数字进行交换。

一开始做的时候，没有处理好一点细节，导致一直没AC过去。

好的做法是画个内存中数组分配的图，就一目了然了！

## AC代码
```C++
class Solution {
public:
    int maximumSwap(int num) {
        vector<int> nums(10,0);
        int count = 1;
        vector<int> max_index(10,1); 
        while(num){
            nums[count] = num%10;
            if(nums[count]>nums[max_index[count-1]]){
                max_index[count] = count;
            }else{
                max_index[count] = max_index[count-1];
            }
            count ++;
            num /=10 ;
        }

        for(int i=count-1;i>=1;i--){
            if(nums[max_index[i]]!=nums[i]){
                swap(nums[i],nums[max_index[i]]);
                break;
            }
        }
        
        int result=0,tens =1;
        for(int i=1;i<count;i++){
            result += nums[i]*tens;
            tens *= 10;
        }
        return result;
    }
    
};
```