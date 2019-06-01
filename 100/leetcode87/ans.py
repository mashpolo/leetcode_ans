#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-01

"""
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[0:i], s2[len(s1) - i:]) and self.isScramble(s1[i:], s2[:len(s1) - i]):
                return True
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.isScramble(s1 = "great", s2 = "rgeat"))
