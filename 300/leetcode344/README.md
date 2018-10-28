# 反转字符串

> 编写一个函数，其作用是将输入的字符串反转过来。

```
示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
```

## 解决思路：
1. 对于python来说，直接考虑切片下的反转即可

### 其他办法：
1. 考虑两个指针分别指向首位，调换位置，直接到中间位置即可

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s)//2):
            tmp = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = tmp

        return ''.join(s)
```

2. 上面的思路，递归

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        left_s = s[:len(s)//2]
        right_s = s[len(s)//2:]
        return self.reverseString(right_s) + self.reverseString(left_s)
```