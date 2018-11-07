# 取暖器
> 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

> 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。

> 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

```
说明:

给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。
示例 1:

输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
```


## 解决思路：
1. 循环判断每个house与所有的取暖器的半径，取最小的值，然后循环完house后，取最大的值---**超时**


### 其他解决思路：
1. 使用二分查找
```
升序排列加热器的坐标heaters

遍历房屋houses，记当前房屋坐标为house：

    利用二分查找，分别找到不大于house的最大加热器坐标left，以及不小于house的最小加热器坐标right

    则当前房屋所需的最小加热器半径radius = min(house - left, right - house)

    利用radius更新最终答案ans
```

```python
class Solution1(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        maxidx=0
        index=0
        for i in range(len(houses)):
            while index+1<len(heaters) and (abs(heaters[index+1]-houses[i])<=abs(heaters[index]-houses[i])):
                index+=1
            maxidx=max(maxidx,abs(heaters[index]-houses[i]))
        return maxidx
```
