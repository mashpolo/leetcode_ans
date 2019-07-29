#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-29

"""


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

        

if __name__ == '__main__':
    A = Solution()
    print(A.largestNumber([7543,5328,9834,1940,9387,871,5208,7,543]))
