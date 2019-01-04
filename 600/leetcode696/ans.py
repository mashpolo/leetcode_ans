#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-1-3

"""


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev_length = 0
        cur_length = 1
        for i in range(1, len(s)):
            print(s[i], s[i-1])
            if s[i] == s[i - 1]:
                cur_length += 1
            else:
                prev_length = cur_length
                cur_length = 1
            if prev_length >= cur_length:
                result += 1
            print(result)
        return result


if __name__ == '__main__':
    A = Solution()
    print(A.countBinarySubstrings('00110011'))
