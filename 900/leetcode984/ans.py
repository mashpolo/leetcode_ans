#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-22

"""


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        result=''
        while A>0 or B>0:
            if A<B:
                result+='b'*min(2,B)+'a'*max(0,min(1,A))
                B-=2
                A-=1
            elif A==B:
                result+='ab'
                A-=1
                B-=1
            else:
                result+='a'*min(2,A)+'b'*max(0,min(1,B))
                A-=2
                B-=1
        return result


if __name__ == '__main__':
    A = Solution()
    print(A.strWithout3a3b(24,31))
