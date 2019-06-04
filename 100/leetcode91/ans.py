#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-06-04

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * (len(s) + 1)  # dp[i]表示以s[0...i)的最多解码方式
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if int(s[i - 1]) != 0:
                if i == 1:
                    dp[i] = 1
                else:
                    if int(s[i - 2]) and int(s[i - 2:i]) <= 26:
                        dp[i] = dp[i - 2] + dp[i - 1]
                    else:
                        dp[i] = dp[i - 1]
            else:
                if i > 1 and 0 < int(s[i - 2:i]) <= 26:
                    dp[i] = dp[i - 2]
                else:
                    return 0

        return dp[len(s)]


if __name__ == '__main__':
    A = Solution()
    print(A.numDecodings("226"))
