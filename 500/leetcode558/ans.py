#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-27

"""


class Solution(object):
    def intersect(self, q1, q2):
        """
        :type q1: Node
        :type q2: Node
        :rtype: Node
        """
        if q1.isLeaf:
            return q1 if q1.val else q2
        if q2.isLeaf:
            return q2 if q2.val else q1

        q1.topLeft = self.intersect(q1.topLeft, q2.topLeft)
        q1.topRight = self.intersect(q1.topRight, q2.topRight)
        q1.bottomLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
        q1.bottomRight = self.intersect(q1.bottomRight, q2.bottomRight)

        if q1.topLeft.isLeaf and q1.topRight.isLeaf and q1.bottomLeft.isLeaf and q1.bottomRight.isLeaf:
            if q1.topLeft.val == q1.topRight.val == q1.bottomLeft.val == q1.bottomRight.val:
                q1.isLeaf = True
                q1.val = q1.topLeft.val
        return q1
