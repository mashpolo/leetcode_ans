#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-26

"""


class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]

        from collections import defaultdict
        d = defaultdict(int)

        res = 0
        for t in time:
            # 1、先计数
            # 针对 [0, 0, 0] 这一类特殊用例，要模 60
            residue = (60 - t) % 60
            if residue in d:
                res += d[residue]

            # 2、再记录频数
            d[t] += 1

        return res


if __name__ == '__main__':
    A = Solution()
    print(A.numPairsDivisibleBy60([60,60,60]))

