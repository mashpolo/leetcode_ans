#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-10

"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = len(nums)
        nums.sort()
        for i in range(l-3):
            if i==0 or nums[i]>nums[i-1]:#去重
                for j in range(i+1,l-2):
                    if j==i+1 or nums[j]>nums[j-1]:#去重
                        left = j+1
                        right = l-1
                        while left<right:
                            indent = nums[i]+nums[j]+nums[left]+nums[right]
                            if indent==target:
                                res.append([nums[i],nums[j],nums[left],nums[right]])
                                left+=1
                                right-=1
                                while left<right and nums[left]==nums[left-1]:#去重
                                    left+=1
                                while left<right and nums[right]==nums[right+1]:#去重
                                    right-=1
                            elif indent<target:
                                left+=1
                            else:
                                right-=1
        return res

