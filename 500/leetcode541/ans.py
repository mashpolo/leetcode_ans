#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-23

"""


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = list(s)
        if len(st) < k:
            return s[::-1]
        if k <= len(st) <= 2*k:
            res = []
            l_st = st[:2*k]
            res.extend(l_st[:k][::-1])
            res.extend(l_st[k:2*k])
            r_st = st[2*k:][::-1]
            res.extend(r_st)
            return "".join(res)
        if len(st) > 2*k:
            res = []
            while len(st) > 2*k:
                l_st = st[:2*k]
                res.extend(l_st[:k][::-1])
                res.extend(l_st[k:2*k])
                st = st[2*k:]
            if len(st) < k:
                res.extend(st[::-1])
            else:
                res.extend(st[:k][::-1])
                res.extend(st[k:])
            return "".join(res)


if __name__ == '__main__':
    A = Solution()
    print(A.reverseStr("abcdefg"
,2))
