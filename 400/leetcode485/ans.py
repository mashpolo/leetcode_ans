#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-10

"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        res = []
        for x in nums:

            if x != 1:
                res.append(n)
                n = 0
            else:
                n += x
        res.append(n)
        return max(res) if res else 0


if __name__ == '__main__':
    A = Solution()
    print(A.findMaxConsecutiveOnes([1,1,0,1,1,1]))
