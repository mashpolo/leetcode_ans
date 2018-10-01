#!/usr/bin/env python
# coding=utf-8
"""
@desc:   缺失数字
@author: Luo.lu
@date:   2018-10-1

"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums.sort()
        for index, x in enumerate(nums):
            if index != x:
                return index
        return len(nums)


if __name__ == '__main__':
    A = Solution()
    print(A.missingNumber([0]))