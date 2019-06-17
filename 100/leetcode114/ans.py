#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-17

"""


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (root.left is None and root.right is None):
            return
        else:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left is None:
                return
            else:
                temp = root.right
                root.right = root.left
                root.left = None
                p = root.right
                while p.right != None:
                    p = p.right
                p.right = temp
                return
