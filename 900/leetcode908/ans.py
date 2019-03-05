#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-05

"""


class Solution:
    def smallestRangeI(self, A, K):
        if not K:
            return max(A) - min(A)

        mid_num = (max(A) + min(A)) >> 1
        if min(A) + K >= mid_num:
            min_new = mid_num
        else:
            min_new = min(A) + K
        if max(A) - K <= mid_num:
            max_new = mid_num
        else:
            max_new = max(A) - K
        return max_new - min_new


if __name__ == '__main__':
    A = Solution()
    print(A.smallestRangeI([1,3,6], 3))


