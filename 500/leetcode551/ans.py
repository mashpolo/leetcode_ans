#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-25

"""
import collections


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c = collections.Counter(s)
        if c['A'] <= 1:
            if 'LLL' not in s:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    A = Solution()
    print(A.checkRecord("PPALLL"))

