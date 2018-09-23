#!/usr/bin/env python
# coding=utf-8
"""
@desc:   用队列实现栈
@author: Luo.lu
@date:   2018-9-23

"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        return self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.pop() if self.stack else None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


if __name__ == "__main__":
    x = 3
    obj = MyStack()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()