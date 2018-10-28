# 反转字符串中的元音字符

> 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

```
示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
```

**说明:**
> 元音字母不包含字母"y"。

## 解决思路：
1. 把字符串转成数组，把元音字符和位置都记录下来，反转元音字符，按照位置添加进去即可


### 其他办法：
1. 思路一里面要顺序记录出现的元音字母和位置，但是在第二遍循环时只用考虑记录这些位置上的字母的变化。
其实也可以只顺序记录所有的元音字母，第二遍循环重新遍历原始字符串，将遇到的元音字母替换成刚才记录的逆序排列。

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
```

2. 维护两个指针分别从字符串头和尾扫描，每次交换两个指针扫到的元音字母，于是只需遍历一遍字符串就可以完成元音字母逆序

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a': True, 'o': True, 'e': True, 'i': True, 'u': True, 'A': True, 'O': True, 'E': True, 'I': True, 'U': True}
        res = list(s)
        pos = []
        for i in xrange(len(res)):
            if res[i] in vowels:
                pos.append((i, res[i]))
        for j in xrange(len(pos)/2):
            res[pos[j][0]] = pos[len(pos)-j-1][1]
            res[pos[len(pos)-j-1][0]] = pos[j][1]
        return ''.join(res)
```