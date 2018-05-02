---
title:  Leetcode-Input array is sorted
date: 2017-11-01 13:52:02
categories: Leetcode
tags: 
 - Array
 - 二分查找
---

# 题目描述
[ Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
```
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```
<!--more-->

# 分析
## O(nlogn)
由于是已经排好顺序的，而且**只存在一组解**，所以最初的想法就是遍历数组，对于每隔遍历的值，再二分查找，有没有可以使得成立的结果。这样的方案就是O(nlogn)的算法了。

## O(n)
后来看了评论区，发现可以O(n)实现。有两个游标，first和last，起始的时候，first指向第一个，last指向最后一个。然后相加，如果两数之和大于target则，last向前移动，如果小于则first向后移动，直到相等。

## O(logn)
这个是对上面的算法进一步进行的优化。因为上面的游标是一个一个移动的，而整个数组又是有序的，所以就可以考虑通过二分查找来快速定位到最接近target情况的游标位置。

引用一个老外的举例解释：

>the standard O(N) solution uses left++ and right-- to move the pointers to the desired solution. This can be made more efficient, in O(log(N)) as mentioned, by not moving the pointers one step at a time, but many steps at a time using binary search.
>
>Essentially what the functions largestSmallerOrLastEqual() and its counterpart do is instead of doing left++ until the sum gets too high, instead do a binary search for the first position for which this holds true also.
>
>Suppose we take the input [1, 2, 3, ... , 1_000_000], i.e, the first million numbers, with target 1_999_999. The solution for that is the last two positions, because 999_999 + 1_000_000 = 1_999_999.
>
>In the O(N) solution this would mean doing left++ 999_998 times! Instead, smallestLargerOrFirstEqual() does a binary search for target - numbers[start] = 1_000_000 - 1 = 999_999, and finds this in only about 20 steps!

# AC代码
## O(nlogn)
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int length = numbers.size();
        vector<int> result;
        for(int i=0;i<length;i++){
            int index2 = find_other_num(numbers,target-numbers[i]);
            if(index2!=-1){
                if (index2==i)
                    index2 = i+1;
                result.push_back(i+1);
                result.push_back(index2+1);
                break;
            }
        }
        return result;
    }
    
    int find_other_num(vector<int>& numbers,int key){
        int low = 0;
        int high = numbers.size()-1;
        while(low<=high){
            int mid = (low+high)/2;
            if(numbers[mid] == key)
                return mid;
            else if (numbers[mid]<key)
                low = mid+1;
            else
                high = mid-1;
        }
        return -1;
    }
    
};
```
## O(n)
```C++
vector<int> twoSum(vector<int>& numbers, int target) {
        
        int l = 0;
        int r = numbers.size() -1;
        while(l < r){
            if(numbers[l] + numbers[r] == target){
                vector<int> res{l+1,r+1};
                return res;
            }
            else if(numbers[l] + numbers[r] > target){
                r--;
            }
            else{
                l++;
            }
        }
    }
```


## O(logn)
```java
public int[] twoSum(int[] numbers, int target) {
        if (numbers == null || numbers.length == 0) {
            return new int[2];
        }
        int start = 0;
        int end = numbers.length - 1;
        while (start < end) {
            if (numbers[start] + numbers[end] == target) {
                return new int[]{start + 1, end + 1};
            } else if (numbers[start] + numbers[end] > target) {
                // move end forward to the last value that numbers[end] <= target - numbers[start]
                end = largestSmallerOrLastEqual(numbers, start, end, target - numbers[start]);
            } else {
                // move start backword to the first value that numbers[start] >= target - numbers[end]
                start = smallestLargerOrFirstEqual(numbers, start, end, target - numbers[end]);
            }
        }
        return new int[2];
    }
    private int largestSmallerOrLastEqual(int[] numbers, int start, int end, int target) {
        int left = start;
        int right = end;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (numbers[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }
    private int smallestLargerOrFirstEqual(int[] numbers, int start, int end, int target) {
        int left = start;
        int right = end;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (numbers[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
```