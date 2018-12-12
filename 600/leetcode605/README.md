# 种花问题

> 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

> 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

```
示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
```

## 解决办法：
1. 采用分割字符串的方式，将0都截取出来，然后就是数学思想了，减去一个1和2整除
2. 需要注意的点是，如果首位都是0的话，应该用'10'和'01'来补充


### 其他思路：
1. 采用贪心算法，从左向右遍历flowerbed，将满足要求的0设为1。计数与n比较即可

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        for i, v in enumerate(flowerbed):
            if v: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            ans += 1
            flowerbed[i] = 1
        return ans >= n
```
