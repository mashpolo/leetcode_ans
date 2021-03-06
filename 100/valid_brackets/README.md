# 判断括号字符串是否正确

> 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

> 有效字符串需满足：

- 左括号必须用相同类型的右括号闭合。
- 左括号必须以正确的顺序闭合。
- 注意空字符串可被认为是有效字符串。

```
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
```

## 解决思路：
> 1. 把括号一一匹配成字典
> 2. 利用栈的思路，字符串转成列表，for循环读取列表数据

- 当前字符是key：字符就入栈
- 当前字符不是key：1. 如果栈空返回False，因为没有左部分可进行匹配了或者左右字符不匹配，返回False，2. 如果遍历完字符串，栈中还有字符，就是还有左部分的字符没有也无法再进行匹配