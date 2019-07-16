#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-16

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        ans = ListNode(0)
        h = ListNode(l[0])
        ans.next = h
        
        for i in range(1, len(l)):
            h.next = ListNode(l[i])
            h = h.next
        return ans.next



