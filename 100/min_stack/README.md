# 最小栈的设计
> 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

```
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

## 解决思路：
1. 对python而言，设计栈就是一个列表而已，需要注意的地方在于还需要一个指针来跟踪最小值
2. 我这边使用了一个新的列表，来存取新加入的最小值（和当前最小值列表的最新值比较，大于和等于都需要append进去）
