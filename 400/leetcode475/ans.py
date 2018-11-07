#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-7

"""


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = []
        for x in houses:
            res.append(min(map(lambda y: abs(x-y), heaters)))
        return max(res)


if __name__ == '__main__':
    A = Solution()
    print(A.findRadius([1,2,3],[2]))

