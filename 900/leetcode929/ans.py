#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-03-10

"""


class Solution:
    def numUniqueEmails(self, emails):
        map_emails = {}
        res = []
        for _mail in emails:
            pre = _mail.split("@")[0].split("+")[0].replace(".", "")
            suf = _mail.split("@")[-1]
            if suf in map_emails:
                if pre not in map_emails[suf]:
                    res.append(_mail)
            else:
                map_emails[suf] = pre
                res.append(f"{pre}@{suf}")

        return len(res)


if __name__ == '__main__':
    A = Solution()
    print(A.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


