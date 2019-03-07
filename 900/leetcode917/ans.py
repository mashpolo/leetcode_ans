#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-07

"""


class Solution:
    def reverseOnlyLetters(self, S):
        first = 0
        end = len(S) - 1
        res = list(S)
        while first < end:
            if res[first].isalpha() and res[end].isalpha():
                res[first], res[end] = res[end], res[first]
                first += 1
                end -= 1
            elif not res[first].isalpha() and res[end].isalpha():
                first += 1
            elif not res[end].isalpha() and res[first].isalpha():
                end -= 1
            else:
                first += 1
                end -= 1
        return "".join(res)


if __name__ == '__main__':
    A = Solution()
    print(A.reverseOnlyLetters("a-bC-dEf-ghIj"))
