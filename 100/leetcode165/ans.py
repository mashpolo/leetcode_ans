#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-25

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = ([*map(int, v.split('.'))] for v in (version1, version2))
        d = len(v2) - len(v1)
        v1, v2 = v1 + [0] * d, v2 + [0] * -d
        return (v1 > v2) - (v1 < v2)


if __name__ == '__main__':
    A = Solution()
    print(A.compareVersion(version1 = "0.1", version2 = "1.1"))
