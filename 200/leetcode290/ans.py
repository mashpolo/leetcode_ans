#!/usr/bin/env python
# coding=utf-8
"""
@desc:   单词模式
@author: Luo.lu
@date:   2018-10-3

"""


class Solution:
    def wordPattern(self, pattern, word):
        """
        :type pattern: str
        :type word: str
        :rtype: bool
        """
        map_dict = {}
        l1 = list(pattern)
        l2 = word.split()
        if len(l1) != len(l2):
            return False
        for index, x in enumerate(l1):
            if x not in map_dict:
                if l2[index] not in map_dict.values():
                    map_dict[x] = l2[index]
                else:
                    return False
            else:
                if map_dict[x] != l2[index]:
                    return False

        return True


if __name__ == '__main__':
    A = Solution()
    print(A.wordPattern('abba', 'dog cat cat dog'))