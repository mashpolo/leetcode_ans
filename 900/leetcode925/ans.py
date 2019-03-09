#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-09

"""


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i,j=0,0
        n,m = len(name),len(typed)
        last =None
        while i<n and j<m:
            if name[i]==typed[j]:
                last = name[i]
                i+=1
                j+=1
            elif typed[j]==last:
                j+=1
            else:return False
        while j<m and typed[j]==last:
            j+=1
        return i==n and j==m


if __name__ == '__main__':
    A = Solution()
    print(A.isLongPressedName(name = "alex", typed = "aaleex"))



