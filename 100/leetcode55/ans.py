#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-08

"""


class Solution:
    def canJump(self, nums) -> bool:
        max_step = 0
        for sec,val in enumerate(nums):
            max_step = max(max_step - 1,val)
            if max_step >= len(nums) - sec -1:
                return True
            elif max_step == 0:
                return False
        return True

