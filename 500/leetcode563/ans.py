#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-1

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            res += self.node_abs(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res

    def node_abs(self, node):
        if node.left:
            lnodes = [node.left]
        else:
            lnodes = None
        if node.right:
            rnodes = [node.right]
        else:
            rnodes = None
        lres = 0
        rres = 0
        while lnodes:
            lnode = lnodes.pop()
            lres += lnode.val
            if lnode.left:
                lnodes.append(lnode.left)
            if lnode.right:
                lnodes.append(lnode.right)
        while rnodes:
            rnode = rnodes.pop()
            rres += rnode.val
            if rnode.left:
                rnodes.append(rnode.left)
            if rnode.right:
                rnodes.append(rnode.right)
        return abs(lres - rres)


if __name__ == '__main__':
    A = Solution()
