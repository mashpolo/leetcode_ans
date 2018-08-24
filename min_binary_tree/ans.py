#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: luluo
@date:   2018-8-24

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        num = 1
        while queue:
            flag = []
            for x in queue:
                print(queue)
                if x.left is None and x.right is None:
                    return num
                else:
                    if x.left is not None:
                        flag.append(x.left)
                    if x.right is not None:
                        flag.append(x.right)
            num += 1
            queue = flag
        return num


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e

A = Solution()
print(A.minDepth(a))