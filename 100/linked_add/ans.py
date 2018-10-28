#!/usr/bin/env python
# coding=utf-8
"""
@desc:   两个链表组合起来的数字相加
@author: luluo
@date:   2018/7/29

"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''.join([str(x) for x in l1[::-1]])
        num2 = ''.join(str(x) for x in l2[::-1])
        if num1[0] == '0' or num2[0] == '0':
            return False
        else:
            result = int(num1) + int(num2)
            res_list = [x for x in str(result)][::-1]
            real_res_list = [int(x) for x in res_list]
            return real_res_list


a = Solution()
print(a.addTwoNumbers([2, 4, 3], [5, 6, 4]))