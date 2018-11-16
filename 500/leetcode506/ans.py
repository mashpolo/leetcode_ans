#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-16

"""


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_bak = sorted(nums)
        map_rs = {}
        for (index, x) in enumerate(nums_bak):
            if index + 3 == len(nums_bak):
                map_rs[x] = "Bronze Medal"
            elif index + 2 == len(nums_bak):
                map_rs[x] = "Silver Medal"
            elif index + 1 == len(nums_bak):
                map_rs[x] = "Gold Medal"
            else:
                map_rs[x] = str(len(nums) - index)
        res = []
        for x in nums:
            res.append(map_rs[x])

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.findRelativeRanks([5, 4, 3, 2, 1]))

