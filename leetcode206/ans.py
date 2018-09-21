#!/usr/bin/env python
# coding=utf-8
"""
@desc:   反转链表
@author: Luo.lu
@date:   2018-9-21

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        before = head
        now = head.next
        while now:
            after = now.next
            now.next, before = before, now
            if after:
                now = after
            else:
                break
        head.next = None
        return now


if __name__ == "__main__":
    head1 = ListNode(0)
    now1 = head1
    for x in range(1, 5):
        b = ListNode(x)
        now1.next = b
        now1 = b

    A = Solution()
    rest = A.reverseList(head1)
    while rest:
        print(rest.val)
        rest = rest.next