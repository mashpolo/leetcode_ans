#!/usr/bin/env python
# coding=utf-8
"""
@desc:   翻转整数
@author: luluo
@date:   2018/7/23

"""


class Solution:
    def reverse(self, num):
        max_num = 2**31 - 1
        min_num = -2**31

        # 小于0的负数
        if num != 0:
            ans_abs = str(abs(num))[::-1]
            ans_str = ""
            for (x, y) in enumerate(ans_abs):
                if x == 0 and y == '0':
                    continue
                elif x > 0 and ans_abs[x-1] == '0' and ans_abs == '0' and y == '0':
                    continue
                else:
                    ans_str += y
                # print(ans_str)
            if num < 0:
                ans = 0 - int(ans_str)
            else:
                ans = int(ans_str)

        else:
            ans = 0

        if ans > max_num or ans < min_num:
            return 0
        else:
            return ans


test_obj = Solution()
print(test_obj.reverse(-2147483648))
