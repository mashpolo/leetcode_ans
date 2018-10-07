#!/usr/bin/env python
# coding=utf-8
"""
@desc:   两个数组的交集
@author: Luo.lu
@date:   2018-10-7

"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    A = Solution()
    print(A.intersection([1,2,2,1], [2,2]))