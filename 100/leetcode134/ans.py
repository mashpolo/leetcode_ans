#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-07-03

"""


class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        if not gas or not cost:
            return -1
        for i in range(len(gas)):
            gas_new = gas[i:] + gas[:i]
            cost_new = cost[i:] + cost[:i]
            begin = 0
            j = 0
            while j <= len(gas) - 1:
                begin += gas_new[j]
                begin -= cost_new[j]
                if begin < 0:
                    break
                j += 1
            if begin >= 0:
                return i
        return -1
    

if __name__ == '__main__':
    A = Solution()
    print(A.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    
    
