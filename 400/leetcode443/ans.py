#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2018-10-30

"""
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        last = 1
        res = []
        for (index, x) in enumerate(chars):
            print(index, x)
            if x in res:
                last += 1
                if index +1 == len(chars):
                    res.append(str(last))
            else:
                if last > 1:
                    res.append(str(last))
                last = 1
                res.append(str(x))
        return res


if __name__ == '__main__':
    A = Solution()
    print(A.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
