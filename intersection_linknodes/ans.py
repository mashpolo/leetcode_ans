#!/usr/bin/env python
# coding=utf-8
"""
@desc:   判断两个链表是否相交
@author: luluo
@date:   2018-9-3

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            if p1:
                flag = p1.val
            if p2:
                flag = p2.val
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
        print(flag)
        # return flag


headA = ListNode(2)
headA.next = ListNode(3)
headA.next.next = ListNode(5)
headA.next.next.next = ListNode(6)
headB = ListNode(1)
headB.next = ListNode(4)
headB.next.next = ListNode(6)

A = Solution()
print(A.getIntersectionNode(headA, headB))
