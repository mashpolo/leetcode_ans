# 最近的请求次数

> 写一个 RecentCounter 类来计算最近的请求。

> 它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。

> 返回从 3000 毫秒前到现在的 ping 数。

> 任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。

> 保证每次对 ping 的调用都使用比之前更大的 t 值。


```
示例：

输入：inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
输出：[null,1,2,3,3]


提示：

每个测试用例最多调用 10000 次 ping。
每个测试用例会使用严格递增的 t 值来调用 ping。
每次调用 ping 都有 1 <= t <= 10^9。

```


## 解决办法：
1. 题意没有理解，根据别人的解决方案了解到

```
第一组是(RecentCounter, [])这个意思我觉得是创立一个RecentCounter型的指针并返回，就如这个函数RecentCounter* recentCounterCreate()
第二组是(ping, [1])调用了ping函数，就是这个int recentCounterPing(RecentCounter* obj, int t) ，1时刻和它之前的1-3000时刻之内都应记录好，其实应该是从0开始递增下去的吧，1-3000到1内的负数不用考虑，所以返回值是1；
第三组是(ping, [100])，(100 - 3000, 100)这个范围之内的值都应记录起来，就是要包括第二组的
(ping, [1])，所以返回值是2；
第四组是(ping, [3001])，(3001 - 3000, 3001)这个范围之内，也就是包括了第二组的(ping, [1])和第三组的(ping, [100])，返回值是3；
第五组是(ping, [3002])，(3002 - 3000, 3002)这个范围之内，也就是包括了第三组的(ping, [100])和第四组的(ping, [3001])，第二组的(ping, [1])不在范围内，舍掉，此时返回值是3
```

2. 也可以直接使用队列，队列中维护当前时间[t-3000,t]这个区间的全部元素，最后返回的结果就是这个队列的长度。

```python
class RecentCounter:

    def __init__(self):
        self.que = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)
```
