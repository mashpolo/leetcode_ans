#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-5

"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        if sort_nums == nums:
            return 0
        first = last = 0
        for (index, x) in enumerate(nums):
            if x != sort_nums[index]:
                print(index)
                first = index
                break
        print(first)
        rev_nums = sort_nums[::-1]
        ma_nums = nums[::-1]
        print(rev_nums)
        for (index, x) in enumerate(ma_nums):
            if x != rev_nums[index]:
                last = index
                print(nums.index(x))
                print(last)
                break

        return len(nums) - last - first


if __name__ == '__main__':
    A = Solution()
    print(A.findUnsortedSubarray([1,2,3,4]))
