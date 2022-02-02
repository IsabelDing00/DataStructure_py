# -*- Coding = utf-8 -*-
# @Author: Isabel Ding


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

'''
      E
 A       G
   C       F
 B   D   

'''
from collections import deque

root = e
# 递归的方式
def pre_order(root):    # 前序遍历：E,A,C,B,D,G,F,
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):     # 中序遍历：A,B,C,D,E,G,F,
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

def back_order(root):   # 后序遍历：B,D,C,A,F,G,E,
    if root:
        back_order(root.lchild)
        back_order(root.rchild)
        print(root.data, end=",")

def level_order(root): # 层次遍历：E,A,G,C,F,B,D,
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # if the length of the tree is not 0
        node = queue.popleft()
        print(node.data, end=",")
        if node.lchild:  # if this node has left child
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)



pre_order(root)
print("")
in_order(root)
print("")
back_order(root)
print("")
level_order(root)
