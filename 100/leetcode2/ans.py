#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-28

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = reversed(l1)
        list2 = reversed(l2)
        now = ListNode(0)
        flag = 0
        while list1 or list2:
            if list1:
                list1_val = list1.val
            else:
                list1_val = 0
            if list2:
                list2_val = list2.val
            else:
                list2_val = 0
            new = list1_val + list2_val + flag
            if new > 9:
                flag = 1
                new = new % 10
            else:
                flag = 0
                new = new
                now.next = ListNode(new)
        return now.next


    def reverse_listnode(self, node):
        cur = node
        tmp = None
        newhead = None
        while cur:
            tmp = cur.next
            cur.next = newhead
            newhead = cur
            cur = tmp

        return newhead

if __name__ == '__main__':
    A = Solution()
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    while a:
        print(a.val)
        a = a.next
