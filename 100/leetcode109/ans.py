#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-16

"""


class Solution(object):
    # 本题采用快慢指针法来获取链表的中间结点
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        # 主体还是用动态规划方法
        def buildBST(head, tail):
            if head == tail:
                return
            # 分别定义快慢指针
            slow = head
            fast = head
            # 此处是为了获得链表的中间结点，即slow
            while fast.next is not tail and fast.next.next is not tail:
                slow = slow.next
                fast = fast.next.next
            pNode = TreeNode(slow.val)
            pNode.left = buildBST(head, slow)
            pNode.right = buildBST(slow.next, tail)
            return pNode
        return buildBST(head, None)

