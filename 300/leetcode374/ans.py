#!/usr/bin/env python
# coding=utf-8
"""
@desc:  猜数字大小
@author: Luo.lu
@date:   2018-10-11

"""


def guess(num):
    if num > 6:
        return -1
    if num < 6:
        return 1
    if num == 6:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        flag = True
        while flag:
            num = guess((high+low) // 2)
            if num == 0:
                return (high + low) // 2
            elif num == -1:
                high = (high + low) // 2 + 1
            elif num == 1:
                low = (high + low) // 2 - 1


if __name__ == '__main__':
    A = Solution()
    print(A.guessNumber(10))



