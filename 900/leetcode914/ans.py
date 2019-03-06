#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-06

"""
from collections import Counter


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = Counter(deck)
        min_num = min(count.values())
        for x in range(2, min_num + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False


if __name__ == '__main__':
    A = Solution()
    print(A.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2,3]))
