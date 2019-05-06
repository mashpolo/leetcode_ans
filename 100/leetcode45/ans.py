#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-06

"""


class Solution:
    def jump(self, nums):
        if (len(nums)==1):
            return 0
        start,end=0,0
        steps=1
        maxindex=0
        while True:
            for i in range(start,end+1):
                maxindex=max(maxindex,nums[i]+i)
            if(maxindex>=len(nums)-1):
                return steps
            steps+=1
            start=end+1
            end=maxindex
