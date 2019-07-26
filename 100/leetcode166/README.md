# 分数到小数

> 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

> 如果小数部分为循环小数，则将循环的部分括在括号内。

```
示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
```

## 解决办法：
1. 主要难点在于求循环小数的部分，需要利用到一个hash表来存储循环部分的值
