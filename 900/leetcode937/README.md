# 重新排列日志文件

> 你有一个日志数组 logs。每条日志都是以空格分隔的字串。

> 对于每条日志，其第一个字为字母数字标识符。然后，要么：

- 标识符后面的每个字将仅由小写字母组成，或；
- 标识符后面的每个字将仅由数字组成。
- 我们将这两种日志分别称为字母日志和数字日志。保证每个日志在其标识符后面至少有一个字。

> 将日志重新排序，使得所有字母日志都排在数字日志之前。字母日志按字母顺序排序，忽略标识符，标识符仅用于表示关系。数字日志应该按原来的顺序排列。

> 返回日志的最终顺序。


```
示例 ：

输入：["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


提示：

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] 保证有一个标识符，并且标识符后面有一个字。
```

## 解决办法：
1. 看题意应该是每个字符串的第二个开始判断，可以分别将是数字和字母的分开，然后再加起来
2. 判断是否是字母可以利用二进制的办法

```python
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig = []
        letter = {}
        for log in logs:
            if ord(log.split()[1][0]) in range(48, 58):
                dig.append(log)
            else:
                letter[log.split(' ', 1)[1]] = log.split(' ', 1)[0]
        result = []
        for key in sorted(letter.keys()):
            s = letter[key] + ' ' + key
            result.append(s)
        result = result + dig
        return result
```
