# 求数组中的唯一不重复的数字
> 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

> 说明：

> 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

```
示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
```

## 解决思路：
1. 使用数学的方法，对不重复的列表求和，再乘以2减去运来的列表的总和即可
2. 更有效率的是使用二进制的位运算方法，采用异或方法，对整个数组类次运算，相同的数抵消，到最后剩下的就是不重复的