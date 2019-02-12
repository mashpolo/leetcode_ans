#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-12

"""


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        first = end = 0
        res = []
        flag = None
        for (index, x) in enumerate(S):
            if x != flag:
                if end - first >= 2:
                    res.append([first, end])
                first = end = index
                flag = x
            else:
                if index == len(S) - 1 and index - first >= 2:
                    res.append([first, index])
                end = index

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.largeGroupPositions("aaa"))


