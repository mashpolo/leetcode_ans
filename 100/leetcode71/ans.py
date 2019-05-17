#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-17

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        res = []
        for p in paths:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if res:
                    res.pop()
                else:
                    res = []
            else:
                res.append(p)
        if not res:
            return '/'
        else:
            return "/" + "/".join(res)


if __name__ == '__main__':
    A = Solution()
    print(A.simplifyPath("/a//b////c/d//././/.."))

