#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-22

"""


class Solution(object):
    def searchRange(self, nums, target):
        low = 0
        high = len(nums) - 1
        if high == -1:
            return [-1,-1]

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = mid
                break
        # 这里已经找到完整的包含target的数组，因此如果数组的最小中还不存在，就说明数组中不存在该数字
        if nums[low] != target:
            return [-1, -1]

        detect = low
        while nums[detect] == target and detect > 0:
            detect -= 1
        if nums[detect] == target:
            buttom = detect
        else:
            buttom = detect + 1

        detect = low
        while nums[detect] == target and detect < len(nums) - 1:
            detect += 1
        if nums[detect] == target:
            top = detect
        else:
            top = detect - 1
        return [buttom, top]
