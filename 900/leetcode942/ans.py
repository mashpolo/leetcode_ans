#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-14

"""


class Solution:
    def diStringMatch(self, S):
        nums = list(range(len(S) + 1))
        A = []
        for x in S:
            if x == 'I':
                A.append(nums[0])
                del nums[0]
            elif x == 'D':
                A.append(nums.pop())
        A.extend(nums)
        return A


if __name__ == '__main__':
    A = Solution()
    print(A.diStringMatch("III"))
