#!/usr/bin/env python
# coding=utf-8
"""
@desc:   删除链表重复的元素
@author: luluo
@date:   2018-8-16

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        pre = head
        cur = head.next
        flag = [head.val]
        while cur:
            if cur.val not in flag:
                flag.append(cur.val)
                pre = cur
                cur = cur.next
            else:

                pre.next = cur.next
                cur = cur.next

        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(1)
a.next = b
b.next = c

print(a.val, a.next.val, a.next.next.val)
A = Solution()
rest = A.deleteDuplicates(a)
print(rest.val, rest.next.val, rest.next.next)
