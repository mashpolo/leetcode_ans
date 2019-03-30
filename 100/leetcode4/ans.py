#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-30

"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res=sorted(res)
        l=len(res)
        if l%2==1:
            return res[l//2]
        else:
            return (res[l//2-1]+res[l//2])/2
