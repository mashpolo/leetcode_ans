#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-22

"""

from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ''

        # 记录t中每个字符在s中出现的次数
        mem = Counter(t)

        t_len = len(t)
        t_uniq = set(t)

        minl, minr = 0, float('inf')

        i = 0
        for j, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1

            print(mem)
            if t_len == 0:
                print(i,j)
                while (s[i] not in t_uniq) or (mem[s[i]] < 0):
                    if mem[s[i]] < 0:
                        mem[s[i]] += 1
                    i += 1
                print(i,j)
                if (minr - minl) > (j - i):
                    minl, minr = i, j
                mem[s[i]] += 1
                i += 1
                t_len += 1

        if minr != float('inf'):
            return s[minl:minr + 1]
        else:
            return ''


if __name__ == '__main__':
    A = Solution()
    print(A.minWindow(s= "ADOBECODEBANC", t= "ABC"))
