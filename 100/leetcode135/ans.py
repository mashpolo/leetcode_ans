#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-04

"""
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        s = 0
        n=len(ratings)
        s+=n
        tmp =[0]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                tmp[i] = tmp[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                tmp[i]=max(tmp[i],tmp[i+1]+1)
        s+=sum(tmp)
        return s
