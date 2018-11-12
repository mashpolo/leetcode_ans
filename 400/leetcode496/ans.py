#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-12

"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map_num = {}
        for (index, x) in enumerate(nums2):
            if index == len(nums2) - 1:
                map_num[x] = -1
            else:
                map_num[x] = nums2[index+1]
        res = []
        for x in nums1:
            key = x
            value = map_num.get(key, -1)
            while value <= x:
                key = map_num[key]
                if key == -1:
                    res.append(key)
                    break
                value = map_num[key]
            if value > 0:
                res.append(value)

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.nextGreaterElement(nums1=[4,1,2], nums2=[1,3,4,2]))
