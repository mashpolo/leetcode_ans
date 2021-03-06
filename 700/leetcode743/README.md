# 网络延迟时间

> 有 N 个网络节点，标记为 1 到 N。

> 给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

> 现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。


> 注意:

- N 的范围在 [1, 100] 之间。
- K 的范围在 [1, N] 之间。
- times 的长度在 [1, 6000] 之间。
- 所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 1 <= w <= 100。


## 解决办法：
1. 采用单源最短路径的算法可以获取，Dijkstra算法


### 其他思路：
1. 弗洛伊德算法，Floyd-Warshall算法

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [[float('inf')] * N for _ in range(N)]
        for time in times:
            u, v, w = time[0] - 1, time[1] - 1, time[2]
            d[u][v] = w
        for i in range(N):
            d[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return -1 if float('inf') in d[K - 1] else max(d[K - 1])
```
