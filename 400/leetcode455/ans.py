#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-2

"""
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        i = 0
        count = 0
        for item in g:
            while i < len(s) and item > s[i]:
                i += 1
            if i == len(s):
                break
            count += 1
            i += 1
        return count


if __name__ == '__main__':
    A = Solution()
    print(A.findContentChildren([10,9,8,7], [5,6,7,8]))
