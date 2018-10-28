#!/usr/bin/env python
# coding=utf-8
"""
@desc:   两个数组的交集
@author: Luo.lu
@date:   2018-10-8

"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        flag = nums1 if len(nums1) < len(nums2) else nums2
        bigger = nums1 if len(nums1) >= len(nums2) else nums2
        res = []
        for x in flag:
            if x in bigger:
                res.append(x)
                index = bigger.index(x)
                bigger[index] = ''

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.intersect([4, 9, 5], [9, 4, 9, 8, 4]))