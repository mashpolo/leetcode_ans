#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-06

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        if len(nums) == 1: return [nums]
        res = list()
        for x in nums:
            ys = list(nums)
            ys.remove(x)
            for y in self.permuteUnique(ys):
                if [x] + y not in res:
                    res.append([x]+y)

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.permuteUnique([1,1,2]))
