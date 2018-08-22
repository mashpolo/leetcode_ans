# 加一
>给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
> 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
> 你可以假设除了整数 0 之外，这个整数不会以零开头。

```
示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
```


## 解决思路
1. 将数组里面的整数转换成字符串，再拼接起来就可以了
2. 字符串转换成整数，再进行操作，然后继续还原成数组就可以了