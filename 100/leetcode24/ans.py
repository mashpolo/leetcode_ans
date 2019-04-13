#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-13

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if not head or not head.next: return head
        cur = head
        head = cur.next
        cur.next = self.swapPairs(head.next)
        head.next = cur
        return head

