#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-28

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = ListNode(float('inf'))  # p 为 head 前一节点
        p.next = head
        ans = p
        while head:
            if head.next is None or head.val != head.next.val:
                p = p.next
                head = head.next
            else:
                while head.next is not None and head.val == head.next.val:
                    head = head.next
                p.next = head.next
                head = head.next
        return ans.next


if __name__ == '__main__':
    head = ListNode(1)
    p = ListNode(float('inf'))
    p.next = head
    for i in [2,2,3,4,4,5]:
        head.next = ListNode(i)
        head = head.next
    A = Solution()
    nums = A.deleteDuplicates(p.next)
    while nums:
        print(nums.val)
        nums = nums.next

