#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-24

"""


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        def maxPath(node):
            nonlocal res
            if not node:
                return 0

            left = max(0, maxPath(node.left))
            right = max(0, maxPath(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val

        maxPath(root)
        return res
