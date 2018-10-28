#!/usr/bin/env python
# coding=utf-8
"""
@desc:   杨辉三角
@author: luluo
@date:   2018-8-26

"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        rest = []
        for level in range(1, numRows + 1):
            if level == 1:
                new = [1]
                last = []
            elif level == 2:
                new = [1, 1]
                last = [1, 1]
            else:
                new = [1, 1]
                for x in range(level):
                    if x == 0 or x == level - 1:
                        continue
                    else:
                        add_num = last[x - 1] + last[x]
                        new.insert(x, add_num)
                last = new
            rest.append(new)
        return rest


A = Solution()
print(A.generate(5))