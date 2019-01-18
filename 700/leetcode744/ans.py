#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-01-18

"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        max_num = ord('z')
        min_num = ord('a')
        target_num = ord(target)
        for x in range(target_num + 1, max_num + 1):
            if chr(x) in letters:
                return chr(x)
        return letters[0]


if __name__ == '__main__':
    A = Solution()
    print(A.nextGreatestLetter(["c","f","j"],"a"))

