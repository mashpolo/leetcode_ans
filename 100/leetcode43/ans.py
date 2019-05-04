#!/usr/bin/env python
# coding=utf-8
"""
@desc:
@author: Luo.lu
@date:   2019-05-05

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 数字倒过来，因为计算的时候从最低位迭代
        num1=num1[::-1]
        num2=num2[::-1]
        # 创建空列表99*99不超过10000，也就是n位数*m位数不会超过，n+m+1
        LIST = [0] * (len(num1) + len(num2)+1)
        for i in range(len(num1)):
            for j in range(len(num2)):
                LIST[j+i]+=int(num1[i])*int(num2[j])
        # 将本位和进位分别计算然后统一处理
        for i in range(len(LIST)-1):
            INDEX= LIST[i]//10
            LIST[i]=LIST[i]%10
            LIST[i+1]+=INDEX
        # 将计算的结果转化成字符串
        res=''
        for i in LIST:
            res += str(i)
        res = res[::-1].lstrip('0')
        if res:
            return res
        else:
            return "0"

