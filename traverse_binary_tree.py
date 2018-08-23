#!/usr/bin/env python
# coding=utf-8
"""
@desc:   二叉树
@author: luluo
@date:   2018-8-22

"""
import time


class Node(object):
    def __init__(self, val='-1'):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.queue = []  # 用来检验当前节点左右子数是否都存在了，不存在的话，这个节点还能继续使用

    def add(self, val):
        """将每个数依次加入到每个节点中，新增一个节点，就这个节点存入队列，直到这个节点的左右树都已满，从队列中删除该节点"""
        if self.root.val == '-1':
            self.root = Node(val)
            self.queue.append(self.root)
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = Node(val)
                self.queue.append(tree_node.left)
            else:
                tree_node.right = Node(val)
                self.queue.append(tree_node.right)
                self.queue.pop(0)

    def front_sort(self, root):
        """使用递归的方式来前序遍历"""
        if root is None:
            return
        print(root.val)
        self.front_sort(root.left)
        self.front_sort(root.right)

    def front_sort_stack(self, root):
        """使用栈的数据结构来保存每次遍历的节点"""
        if root is None:
            return
        stack = []
        node = root
        while node or stack:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def end_sort(self, root):
        """使用递归的方式来完成后序遍历"""
        if root is None:
            return

        self.end_sort(root.left)
        self.end_sort(root.right)
        print(root.val)

    def end_sort_stack(self, root):
        """使用栈数据结构来实现后序遍历"""
        if root is None:
            return

        stack = [root]
        rest_stack = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            rest_stack.append(node)
        while rest_stack:
            print(rest_stack.pop().val)

    def middle_sort(self, root):
        """使用递归的方式来实现中序遍历"""
        if root is None:
            return

        self.middle_sort(root.left)
        print(root.val)
        self.middle_sort(root.right)

    def middle_sort_stack(self, root):
        """使用栈来实现中序遍历"""
        if not root:
            return

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
            node = node.right

    def level_sort(self, root):
        """使用队列来实现层次的遍历，也就是广度优先遍历"""
        if root is None:
            return

        flag_queue = [root]
        while flag_queue:
            node = flag_queue.pop(0)
            print(node.val)
            if node.left is not None:
                flag_queue.append(node.left)
            if node.right is not None:
                flag_queue.append(node.right)


if __name__ == "__main__":
    """main function"""
    test_tree = Tree()
    for a in range(10000):
        test_tree.add(a)

    print('\n\n递归实现先序遍历:')
    start = time.time()
    test_tree.front_sort(test_tree.root)
    end = time.time()
    print(end - start)
    print('\n\n非递归，利用栈来实现前序遍历')
    start = time.time()
    test_tree.front_sort_stack(test_tree.root)
    end = time.time()
    print(end-start)
    # print('\n递归实现中序遍历:')
    # test_tree.middle_sort(test_tree.root)
    # print('\n\n非递归，使用栈来实现中序遍历')
    # test_tree.middle_sort_stack(test_tree.root)
    # print('\n递归实现后序遍历:')
    # test_tree.end_sort(test_tree.root)
    # print('\n非递归，使用栈来实现后序遍历')
    # test_tree.end_sort_stack(test_tree.root)
    # print('\n层次遍历:')
    # test_tree.level_sort(test_tree.root)




