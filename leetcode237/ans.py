#!/usr/bin/env python
# coding=utf-8
"""
@desc:   删除链表中的节点
@author: Luo.lu
@date:   2018-9-27

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if node.next:
                node.val = node.next.val
                node.next = node.next if node.next.next else None
            node = node.next


if __name__ == "__main__":
    l = ListNode(2)
    l.next = ListNode(0)
    l.next.next = ListNode(1)
    l.next.next.next = ListNode(3)

    k = ListNode(5)
    A = Solution()
    res = A.deleteNode(l)
    while l:
        print(l.val)
        l = l.next

