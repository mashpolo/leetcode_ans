# 七进制数

> 给定一个整数，将其转化为7进制，并以字符串形式输出。

```
示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。
```


## 解决思路：
1. 直接除7求余数，然后反转得到的数即可

```python
class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return "0"
        res=''
        n=abs(num)
        while n:
            res=str(n%7)+res
            n//=7
        return res if num>0 else '-'+res
```
