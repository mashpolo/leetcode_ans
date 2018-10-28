# 实现 strStr() 函数
> 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1

```
示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
```


## 解决思路：
1. 递归寻找一个符合needle字符串长度的块，再和needle比较，相等返回index
2. python中可以直接使用str.find方法