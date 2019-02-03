#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-03

"""


class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = 0
        new = 1
        for (index, x) in enumerate(S):
            tag = widths[ord(x) - 97]
            if res + tag > 100:
                new += 1
                res = tag
            else:
                res += tag

        return [new, res]


if __name__ == '__main__':
    A = Solution()
    print(A.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                          "bbbcccdddaaa"))
