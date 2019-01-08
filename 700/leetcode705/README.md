# 设计哈希集合

> 不使用任何内建的哈希表库设计一个哈希集合

> 具体地说，你的设计应该包含以下的功能

- add(value)：向哈希集合中插入一个值。
- contains(value) ：返回哈希集合中是否存在这个值。
- remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

```
示例:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);
hashSet.contains(2);    // 返回 true
hashSet.remove(2);
hashSet.contains(2);    // 返回  false (已经被删除)

注意：

所有的值都在 [1, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。
```

## 解决办法：
1. 其实就是让设计一个用其他数据结构来表示字典的方法
2. 使用列表来存储，需要注意的是不能有重复值


### 其他思路：

1. 用列表，由于有数字的限制，那么直接存储一个bool值节约内存

```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.set[key]
```

2. 节省内存的写法，常规的思路，设定一个键值来存储变量


```python
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [False] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.set[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.set[key]
```
