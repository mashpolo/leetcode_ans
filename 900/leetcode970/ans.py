#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-20

"""


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ans = []

        for i in range(20):
            for j in range(20):
                a = x ** i + y ** j
                if a <= bound:
                    ans.append(a)

        return list(set(ans))


if __name__ == '__main__':
    A = Solution()
    print(A.powerfulIntegers(x=2, y=3, bound=10))

