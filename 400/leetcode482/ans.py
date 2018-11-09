#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-9

"""


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = S.replace('-', '').upper()
        if not s:
            return s
        list_s = list(s)[::-1]
        res = []
        a = ""
        for (index, x) in enumerate(list_s):
            a += x
            if len(a) == K:
                res.append(a)
                a = ""
            if index == len(list_s) - 1:
                res.append(a)
        res = "-".join(res)[::-1]
        return res if res[0] != '-' else res[1:]


if __name__ == '__main__':
    A = Solution()
    print(A.licenseKeyFormatting(S="---", K=2))
