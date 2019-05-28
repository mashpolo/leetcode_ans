#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-27

"""


class Solution:
    def search(self, nums, target):
        # 寻找拐点
        if not nums: return False
        if len(nums) == 1: return nums[0] == target
        for n in range(1, len(nums)):
            if nums[n] < nums[n - 1]:
                break
        left, right = nums[:n], nums[n:]
        print(left, right)
        return self.two_search(target, left) or self.two_search(target, right)

    def two_search(self, key, c):
        lo, hi = 0, len(c) - 1
        while lo <= hi:
            mid = int(lo + (hi - lo) // 2)
            if key < c[mid]:
                hi = mid - 1
            elif key > c[mid]:
                lo = mid + 1
            else:
                return True
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.search(nums=[2,5,6,0,0,1,2],target=0))

