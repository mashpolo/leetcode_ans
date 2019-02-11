#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-11

"""
import re


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        r = re.compile(r"^[a|e|i|o|u]")
        words = S.split()
        new_word = ""
        for (index, w) in enumerate(words):
            m = r.match(w.lower())
            if m:
                new = w + "ma"
            else:
                new = w[1:] + w[0] + 'ma'

            new += "a" * (index + 1)
            new_word += " "
            new_word += new
        return new_word[1:]


if __name__ == '__main__':
    A = Solution()
    print(A.toGoatLatin("I speak Goat Latin"))
