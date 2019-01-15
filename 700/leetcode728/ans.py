#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-15

"""


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        while left <= right:
            nums = str(left)
            if '0' in nums:
                left += 1
                continue
            for x in nums:
                if x == '0':
                    continue
                if int(left) % int(x) != 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                res.append(left)
            left += 1
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.selfDividingNumbers(left=1, right=22))
