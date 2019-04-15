#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-15

"""


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head

        while cur != None:
            t = cur
            count = 1
            while count < k and t != None:
                t = t.next
                count += 1
            if count == k and t != None:
                for _ in range(k - 1):
                    lat = cur.next
                    cur.next = lat.next
                    lat.next = pre.next
                    pre.next = lat

                pre = cur
                cur = pre.next
            else:
                break

        return h.next
