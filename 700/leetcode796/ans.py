#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-31

"""


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        if len(A) != len(B):
            return False
        flag = B[0]
        right = ''
        while flag in A:
            res = A.index(flag) if flag in A else None
            if res != 0:
                left, last = A[:res], A[res:]
            else:
                left, last = A[0], A[1:]
            new = last + right + left
            print(new)
            if new == B:
                return True
            else:
                A = last
                right += left
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.rotateString("vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg",
"fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"))
