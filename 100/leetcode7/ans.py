#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-02

"""


class Solution:
    def myAtoi(self, str: str) -> int:
        words = str.strip()
        if len(words) == 0 or (not words[0].isdigit()) and (words[0] not in ['-', '+']):
            return 0
        res = [words[0]]
        for x in words[1:]:
            if x.isdigit():
                res.append(x)
            else:
                break
        if res == ["+"] or res == ["-"]:
            return 0
        num = "".join(res)
        if int(num) > 2**31 -1:
            return 2**31
        elif int(num) < -2**31:
            return -2**31
        else:
            return int(num)


if __name__ == '__main__':
    A = Solution()
    print(A.myAtoi("   -5"))


