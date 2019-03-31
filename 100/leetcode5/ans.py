#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-31

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=len(s)

        if(length<=1 or s==s[::-1]):
            return s

        start=0
        maxLen=1
        for i in range(0,length):
            if i-maxLen>=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue
            if i-maxLen>=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1

        return s[start:start+maxLen]


if __name__ == '__main__':
    A = Solution()
    print(A.longestPalindrome('babad'))


