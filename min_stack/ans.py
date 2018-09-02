class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_list:
            self.min_list.append(x)
        else:
            if self.min_list[-1] >= x:
                self.min_list.append(x)
        return self.stack

    def pop(self):
        """
        :rtype: void
        """
        falg = self.stack.pop()
        if falg == self.min_list[-1]:
            self.min_list.pop()
        return self.stack
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_list[-1] if len(self.min_list) > 1 else self.min_list[0]
