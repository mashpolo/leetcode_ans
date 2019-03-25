#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-25

"""


class Solution:
    def isCousins(self, root, x, y):
        q = [root]
        item = 0
        res = {}
        while q:
            q2 = []
            if 'x' in res and 'y' in res:
                break
            for t in q:
                if t.val == x:
                    res['x'] = item
                if t.val == y:
                    res['y'] = item
                if t.left:
                    q2.append(t.left)
                    if t.left.val == x:
                        res['xf'] = t.val
                    if t.left.val == y:
                        res['yf'] = t.val
                if t.right:
                    q2.append(t.right)
                    if t.right.val == x:
                        res['xf'] = t.val
                    if t.right.val == y:
                        res['yf'] = t.val
            item += 1
            q = q2

        return res['x'] == res['y'] and res['xf'] != res['yf']

