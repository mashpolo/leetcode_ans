#!/usr/bin/env python
# coding=utf-8
"""
@desc:   合并两个有序列表
@author: luluo
@date:   2018-8-17

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()

        print(nums1)

        if not nums1:
            for (index, x) in enumerate(nums2):
                nums1.insert(index, x)
        else:
            for x in nums2:
                l = len(nums1)
                for index in range(l):
                    if x >= nums1[l - index - 1]:
                        print('%d is bigger than %d' % (x, nums1[l-index-1],))
                        nums1.insert(l - index, x)
                        break
                    else:
                        print('%d is smaller than %d' % (x, nums1[l-index-1]))
                        if index == l - 1:
                            nums1.insert(0, x)
                            break
                        else:
                            continue

        return nums1


A = Solution()
print(A.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
