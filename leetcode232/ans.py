#!/usr/bin/env python
# coding=utf-8
"""
@desc:   用栈实现队列
@author: Luo.lu
@date:   2018-9-25

"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        return self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0] if self.queue else None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


if __name__ == "__main__":
    x = 'test2'
    obj = MyQueue()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()