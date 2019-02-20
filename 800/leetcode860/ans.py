#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-20

"""
from collections import Counter

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        res = []
        for bill in bills:
            # print(f"res={res}, bill={bill}")
            if bill == 5:
                res.append(bill)
            elif bill == 10:
                if 5 in res:
                    res.remove(5)
                    res.append(bill)
                else:
                    return False
            elif bill == 20:
                if 10 in res and 5 in res:
                    res.remove(10)
                    res.remove(5)
                    res.append(bill)
                elif 5 in res and Counter(res)[5] > 3:
                    res.remove(5)
                    res.remove(5)
                    res.remove(5)
                else:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    A = Solution()
    print(A.lemonadeChange([5,5,5,10,5,5,10,20,20,20]))

