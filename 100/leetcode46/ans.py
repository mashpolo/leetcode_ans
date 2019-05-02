#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-06

"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None: return []
        if len(nums) == 1: return [nums]
        res = []
        for x in nums:
            ys = list(nums)
            ys.remove(x)
            for y in self.permute(ys):
                res.append([x]+y)
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.permute([1,2,3]))
