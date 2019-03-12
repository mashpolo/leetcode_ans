#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-12

"""


class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        nums = list(filter(lambda x: x[x.find(" ")+1].isdigit(), logs))
        alphas = list(filter(lambda x: x[x.find(" ")+1].isalpha(), logs))
        alphas.sort(key=lambda x: x.split()[1:])
        return alphas + nums
