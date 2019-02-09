#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-09

"""
import re


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = re.sub(r"[!|?|'|,|;|\.]", ' ', paragraph.lower())
        words = para.split()
        counts = {}
        print(words)
        for word in words:
            new_word = word
            if new_word in banned:
                continue
            if new_word in counts:
                counts[new_word] += 1
            else:
                counts[new_word] = 1
        res = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True)]
        return res[0][0]


if __name__ == '__main__':
    A = Solution()
    print(A.mostCommonWord("a, a, a, a, b,b,b,c, c",
["a"]))
