#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-26

"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.isspace():
            return  0
        s1 = s.strip()
        if len(s1) == 0:
            return  0
        d =[0]
        m = list(s1)
        while m:
            if m[0] != ' ':
                d[-1] += 1
            else:
                d.append(0)
            m.pop(0)
        return len(d) - d.count(0)


if __name__ == '__main__':
    A = Solution()
    print(A.countSegments(""))
