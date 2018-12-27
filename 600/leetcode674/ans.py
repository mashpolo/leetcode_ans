#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-27

"""


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        res = 0
        for x in nums:
            if not tmp:
                tmp.append(x)
            else:
                if tmp[-1] < x:
                    tmp.append(x)
                else:
                    res = max(res, len(tmp))
                    tmp = [x]
        return max(res, len(tmp))


if __name__ == '__main__':
    A = Solution()
    print(A.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
