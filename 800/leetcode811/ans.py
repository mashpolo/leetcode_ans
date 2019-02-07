#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-07

"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        res = {}
        result = []
        domains = {k:v for k, v in zip([x.split(" ")[1] for x in cpdomains],
                                       [int(y.split(" ")[0]) for y in cpdomains])}
        for key in domains:
            first = ""
            domain = key.split(".")
            domain.reverse()
            for _d in domain:
                flag = _d + "." + first
                if flag in res:
                    first = flag
                    res[flag] += domains[key]
                else:
                    first = flag
                    res[flag] = domains[key]
        for k in res:
            s = str(res[k]) + " " + k
            result.insert(0, s)
        return result


if __name__ == '__main__':
    A = Solution()
    print(A.subdomainVisits(["9001 discuss.leetcode.com"]))

