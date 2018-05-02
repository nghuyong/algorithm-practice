---
title: 剑指offer-链表中倒数第k个数
date: 2018-04-27 13:36:02
categories: 剑指offer
tags: 
---

# 题目描述
输入一个链表，输出该链表中倒数第k个结点。

<!--more-->

# 分析
核心就是有两个指针，一开始都指向链表头节点。
然后移动一个指针向前走k-1步，然后在一起走，这样，前面指针到达最后一个节点的时候，后面的指针正好位于倒数第k个节点.

# 代码

```C++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
// 1->2->3->4->5->6->NULLjavascript:void(0);
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if(pListHead==NULL || k==0){
            return NULL;
        }
        ListNode *p_left,*p_right;
        p_left = p_right = pListHead;
        for(int i=0;i<k-1;i++){
            if(p_right->next==NULL){
                return NULL;
            }else{
                p_right = p_right->next;
            }
        }
        while(p_right->next){
            p_right = p_right->next;
            p_left = p_left->next;
        }
        return p_left;

    }
};
```
