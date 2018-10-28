#!/usr/bin/env python
# coding=utf-8
"""
@desc:   打家劫舍
@author: Luo.lu
@date:   2018-9-16

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            now_len = len(nums)
            last = nums.pop()
            return max(last + self.rob(nums[:now_len - 2]), self.rob(nums[:now_len - 1]))
        """
        now = last = 0
        for i in nums:
            last, now = now, max(i+last, now)
            print(last, now)
        return now


if __name__ == "__main__":
    A = Solution()
    print(A.rob([1, 3, 4, 9]))