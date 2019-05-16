#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-16

"""


class Solution:
    def layout(self, words, curlen, maxWidth, last=False):
        if len(words) == 1:
            return words[0] + ' ' * (maxWidth - len(words[0]))
        if last:
            r = ' '.join(words)
            return r + ' ' * (maxWidth - len(r))
        space = maxWidth - curlen
        space0 = space // (len(words) - 1)
        space1 = space % (len(words) - 1)
        ret = ""
        for i in range(len(words) - 1):
            ret += words[i] + ' ' + ' ' * space0
            if space1:
                ret += ' '
                space1 -= 1
        ret += words[-1]
        return ret

    def fullJustify(self, words, maxWidth):

        ret, s, curlen = [], 0, 0
        for k, v in enumerate(words):
            if curlen + 1 + len(v) > maxWidth:
                if s == k:
                    ret.append(self.layout(
                        words[s:k + 1], curlen, maxWidth))
                    s, curlen = k + 1, 0
                else:
                    ret.append(self.layout(
                        words[s:k], curlen, maxWidth))
                    s, curlen = k, len(v)
            else:
                if curlen:
                    curlen += 1
                curlen += len(v)
        if words[s:]:
            ret.append(self.layout(
                words[s:], curlen, maxWidth, True))

        return ret


if __name__ == '__main__':
    A = Solution()
    print(A.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

