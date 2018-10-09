# 有效的完全平方数

> 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

> 说明：不要使用任何内置的库函数，如  sqrt。

```
示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
```

## 解决思路：
1. 二分法，不断逼近临界值即可


### 其他方法：
1. 牛顿迭代，求平方根可以转化为求函数y = x ^ 2 - num的根，迭代过程x = (x + num / x) * 1/2

```python
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num / x) // 2
        return x * x == num
```
