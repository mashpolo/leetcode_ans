#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-28

"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]


if __name__ == '__main__':
    A = Solution()
    print(A.letterCasePermutation("a1b2"))

