#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-25

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        fast = slow = head
        if not head:
            return slow
        while fast.next:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            if fast.next and not fast.next.next:
                slow = slow.next
                fast = fast.next
        return slow


