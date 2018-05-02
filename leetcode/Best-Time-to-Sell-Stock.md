---
title: Leetcode-Best Time to Buy and Sell Stock
date: 2017-11-02 17:11:02
categories: Leetcode
tags: 
 - Array
---

# 题目描述
[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
```
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
```
<!--more-->

# 分析
这题一开始以为是DP问题，后来发现想复杂了。

其实只需要遍历一次，假设遍历到`nums[i]`,只要找出当前最小的值，然后比较一下`nums[i]`减去当前最小的值能不能活得当前更大的利润。

后来在评论区，发现这个可以转换成，求解连续字串最大和的问题。构造一个新的数列，这里面的值是后一个减去前一个。这样求解这个新数列的字串最大和就是这个问题的解了。

而这个可以采用经典的求解方案：Kadane's algorithm

![](http://onqlxvamk.bkt.clouddn.com/HuYong/WX20171102-171744@2x.png)

# AC代码
减去最小值的思路
```C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        int max_profit = 0;
        int min_num = 0x7fffffff;
        for(int i=0;i<length;i++){
            if(prices[i]<min_num){
                min_num = prices[i];
            }else{
                max_profit = max(max_profit,prices[i]-min_num);
            }
        }
        return max_profit;
    }
};
```


Kadane's algorithm
```java
public int maxProfit(int[] prices) {
    if(prices.length<2) return 0;
    int diff[] = new int[prices.length-1];
    for(int i=1; i<prices.length; i++){
        diff[i-1] = prices[i] - prices[i-1];
    }
    return maxSubArray(diff);
}
public int maxSubArray(int[] nums) {
    if(nums.length<1) return 0;
    int preMax = 0, m = 0;
    for(int i=0; i<nums.length; i++){
        m = Math.max(m, preMax+nums[i]);
        preMax = Math.max(0, preMax+nums[i]);
    }
    return m;
}
```