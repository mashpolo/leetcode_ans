#!/usr/bin/env python
# coding=utf-8
"""
@desc:   
@author: luluo
@date:   2018-8-21

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res

        q = [root]
        while len(q) != 0:
            res.append([node.val for node in q])
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q

        return res[::-1]


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
A.left = B
A.right = C
C.left = D
C.right = E


rest = Solution()
print(rest.levelOrderBottom(A))

