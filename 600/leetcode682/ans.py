#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-12-29

"""


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if not ops:
            return 0
        res = []
        for x in ops:
            if x == '+':
                if len(res) > 1:
                    print(res[-2], res[-1])
                    res.append(res[-1] + res[-2])
                else:
                    res.append(res[0])
            elif x == 'D':
                if len(res) > 0:
                    res.append(int(res[-1]) * 2)
                else:
                    res.append(0)
            elif x == 'C':
                res.pop()
            else:
                res.append(int(x))

        return sum(res)


if __name__ == '__main__':
    A = Solution()
    print(A.calPoints(["5","2","C","D","+"]))
