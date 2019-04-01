#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-04-01

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) < numRows:
            return s
        total = {}
        flag = 1
        status = 1
        for x in s:
            if flag in total:
                total[flag].append(x)
            else:
                total[flag] = [x]
            if flag == numRows:
                status = 0
                flag -= 1
            elif flag == 1:
                status = 1
                flag += 1
            else:
                if status:
                    flag += 1
                else:
                    flag -= 1
        res = ""
        for y in range(1, numRows + 1):
            res += "".join(total[y])
        res += "".join(s[len(res):])
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.convert(s = "LE", numRows = 1))
