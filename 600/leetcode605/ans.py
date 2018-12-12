#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-12

"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        str_num = "".join([str(i) for i in flowerbed])
        if str_num.startswith('0'):
            str_num = "10" + str_num
        if str_num.endswith('0'):
            str_num += "01"
        res = 0
        for x in str_num.split('1'):
            if x:
                res += (len(x)-1) // 2
        return res >= n


if __name__ == '__main__':
    A = Solution()
    print(A.canPlaceFlowers(flowerbed=[1,0,0,0,1,0,0], n=2))
