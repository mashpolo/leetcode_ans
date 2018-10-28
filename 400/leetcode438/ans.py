#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-28

"""
from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if not p or not s:
            return res

        lenP = len(p)
        lenS = len(s)
        if lenS < lenP:
            return res

        hP = defaultdict(int)
        for ch in p:
            hP[ch] += 1
        print(hP)
        count = len(hP.keys())
        print(count)
        for i in range(lenP):
            ch = s[i]
            if ch in hP:
                hP[ch] -= 1
                if hP[ch] == 0:
                    count -= 1

        if count == 0:
            res.append(0)

        left = 0
        right = lenP
        while right < lenS:
            ch = s[right]
            if ch in hP:
                hP[ch] -= 1
                if hP[ch] == 0:
                    count -= 1

            ch = s[left]
            if ch in hP:
                hP[ch] += 1
                if hP[ch] == 1:
                    count += 1

            left += 1
            right += 1
            if count == 0:
                res.append(left)

        return res



if __name__ == '__main__':
    A = Solution()
    print(A.findAnagrams(s="cbaebabacd", p="abc"))

