#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-13

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None: return head
        start, end, len = head, None, 0
        while head:
            end = head
            head = head.next
            len += 1
        end.next = start
        pos = len - k % len
        while pos > 1:
            start = start.next
            pos -= 1
        ret = start.next
        start.next = None
        return ret


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    # n = n1
    # while n:
    #     print(n.val)
    #     n = n.next

    A = Solution()
    nodes = A.rotateRight(n1, 2)
    while nodes:
        print(nodes.val)
        nodes = nodes.next



