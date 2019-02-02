#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-02-02

"""


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        word_dict = {
                    "a": ".-",
                    "b": "-...",
                    "c": "-.-.",
                    "d": "-..",
                    "e": ".",
                    "f": "..-.",
                    "g": "--.",
                    "h": "....",
                    "i": "..",
                    "j": ".---",
                    "k": "-.-",
                    "l": ".-..",
                    "m": "--",
                    "n": "-.",
                    "o": "---",
                    "p": ".--.",
                    "q": "--.-",
                    "r": ".-.",
                    "s": "...",
                    "t": "-",
                    "u": "..-",
                    "v": "...-",
                    "w": ".--",
                    "x": "-..-",
                    "y": "-.--",
                    "z": "--..",
                    }
        res = []
        for word in words:
            word_trans = "".join(map(lambda x: word_dict[x], word))
            res.append(word_trans)

        return len(set(res))


if __name__ == '__main__':
    A = Solution()
    print(A.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
