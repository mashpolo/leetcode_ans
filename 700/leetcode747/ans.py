#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-20

"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        max_num = max(nums)
        index = nums.index(max_num)
        nums.remove(max_num)
        sec_num = max(nums)
        if sec_num * 2 <= max_num:
            return index
        else:
            return -1


if __name__ == '__main__':
    A = Solution()
    print(A.dominantIndex([0,0,1,2]))

