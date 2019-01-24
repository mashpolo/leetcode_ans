# 到达最终数字

> 在一根无限长的数轴上，你站在0的位置。终点在target的位置。

> 每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

> 返回到达终点需要的最小移动次数。

```
示例 1:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
示例 2:

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
```

> 注意:

> target是在[-10^9, 10^9]范围中的非零整数。



## 解决办法：
1. 采用数学的思想，首先是判断一条道走到死的，也就是不用折返走的，直接求和
2. 如果不能直达，那么需要考虑折返跑，算法即是 n**2 + n = target * m（当前循环次数）* 2
