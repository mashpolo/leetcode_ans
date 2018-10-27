#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-27

"""
import collections


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1
        def pSum(root, cur, sum):
            if not root: return 0
            res = 0
            cur += root.val
            if cur - sum in d:
                res += d[cur - sum]
            d[cur] += 1
            res += pSum(root.left, cur, sum) + pSum(root.right, cur, sum)
            d[cur] -= 1
            return res
        return pSum(root, 0, sum)
