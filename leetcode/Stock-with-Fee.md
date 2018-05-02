---
title: Leetcode-Best Time to Buy and Sell Stock with Transaction Fee
date: 2017-11-13 20:04:02
categories: Leetcode
tags: 
 - DP
 - Array
---

# 题目描述
[Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)
```
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

```
<!--more-->

# 分析
这也是一道DP问题。

在第i天，只会有两个状态，手上现在有股票，和手上现在没有股票。分别计算着两者当前获利的最大值。

没有股票 = max(没有股票,卖出股票)

持有股票 = max(持有股票，买进股票)

注意这里买进股票是需要手续费的

对应的原来的[Best Time to Buy and Sell Stock II](https://leetcode.com/submissions/detail/126541669/)也可以用这种方法求解，只是不用减去手续费了。

## AC代码
```C++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
       int s0 = 0, s1 = INT_MIN; 
        for(int p:prices) {
            int tmp = s0;
            s0 = max(s0, s1+p);
            s1 = max(s1, tmp-p-fee);
        }
        return s0;
    }
    
};
```

