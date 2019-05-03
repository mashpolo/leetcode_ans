#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-05

"""


class Solution(object):
    def isMatch(self, s, p):
        len_s, len_p = len(s), len(p)
        if not len_s:
            for alpha in p:
                if alpha != "*":
                    return False
            return True
        if not len_p:
            if not len_s:
                return True
            return False

        f = dict()
        for i in range(-1, len(s)):
            f[i] = dict()
            for j in range(len(p)):
                f[i][j] = False

        if s[0] == p[0] or p[0] == "?":
            f[0][0] = True
        for j in range(0, len_p):
            if p[j] == "*":
                for i in range(-1, len_s):
                    f[i][j] = True
            else:
                break

        for i in range(len_s):
            for j in range(len_p):
                if (s[i] == p[j] or p[j] == "?") and i >= 0 and j > 0:
                    f[i][j] = f[i-1][j-1]
                elif p[j] == "*" and i >= 0 and j > 0:
                    f[i][j] = f[i-1][j] or f[i][j-1]
        return f[len_s-1][len_p-1]


if __name__ == '__main__':
    A = Solution()
    print(A.isMatch(s='aa', p='a?'))
