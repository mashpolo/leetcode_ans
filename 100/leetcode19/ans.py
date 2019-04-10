#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-10

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        first = head
        last = head
        num = 0
        while num != n:
            last = last.next
            num += 1
        if not last:
            head = head.next
            return head
        while last.next:
            last = last.next
            first = first.next
        first.next = first.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # while head:
    #     print(head.val)
    #     head = head.next
    A = Solution()
    aaa = A.removeNthFromEnd(head, n = 2)








