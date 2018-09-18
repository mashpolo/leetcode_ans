#!/usr/bin/env python
# coding=utf-8
"""
@desc:   删除链表中的节点
@author: Luo.lu
@date:   2018-9-18

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        before = now = head
        while now:
            if now.val == val:
                if before == now == head:
                    before = now = head = head.next
                else:
                    now = now.next
                    before.next = now
            else:
                before = now
                now = now.next
        return head


if __name__ == "__main__":
    l = a = ListNode(0)
    # a.next = ListNode(1)
    # a.next.next = ListNode(2)
    for x in range(1, 5):
        l.next = ListNode(x)
        l = l.next
    A = Solution()
    A.removeElements(a, 1)
    while a:
        print(a.val)
        a = a.next