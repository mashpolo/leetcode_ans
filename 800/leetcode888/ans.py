#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-28

"""


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        poor = abs(sum(B) - sum(A))
        min_num = A if sum(A) < sum(B) else B
        max_num = A if sum(A) > sum(B) else A
        if poor & 1:
            return []
        comb = poor // 2
        for x in min_num:
            if x + comb in max_num:
                return [x, x + comb]
