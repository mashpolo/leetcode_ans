#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-31

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x: int):
        if not head:
            return
        small = ListNode(float("inf"))
        large = ListNode(float("inf"))
        first = small
        end = large
        while head:
            if head.val < x:
                print(f"small is {first.val}, {head.val}")
                first.next = head
                first = first.next
            else:
                print(f"large is {end.val}, {head.val}")
                end.next = head
                end = end.next
            head = head.next
        end.next = None

        first.next = large.next
        return small.next


if __name__ == '__main__':
    A = Solution()
    l = [1,4,3,2,5,2]
    p = ListNode(float("inf"))
    n = p
    i = 0
    while i <= len(l) - 1:
        n.next = ListNode(l[i])
        n = n.next
        i += 1
    # while p:
    #     print(p.val)
    #     p = p.next
    res = A.partition(p.next, 3)
    while res:
        print(res.val)
        res = res.next




