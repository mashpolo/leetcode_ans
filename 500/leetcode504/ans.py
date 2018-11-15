#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-11-15

"""


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        if num < 0:
            flag = abs(num)
        elif num == 0:
            return 0
        else:
            flag = num
        while flag > 0:
            d1 = flag % 7
            flag = flag // 7
            res.append(d1)
        if num > 0:
            return "".join(str(x) for x in res[::-1])
        else:
            return "-" + "".join(str(x) for x in res[::-1])


if __name__ == '__main__':
    A = Solution()
    print(A.convertToBase7(100))
