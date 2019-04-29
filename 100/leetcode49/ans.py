#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-06

"""


class Solution(object):
    def groupAnagrams(self, strs):
        m = {}
        for s in strs:
            key = "".join(sorted(s[:]))
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        return list(m.values())


if __name__ == '__main__':
    A = Solution()
    print(A.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))
