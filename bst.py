# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, li=None):
        self.root = None
        if li:   # if li is not None
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):  # 递归的方法
        if not node:  # if node == None
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild,val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchilf, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):   #  不用递归的方法
        p = self.root
        if not p:     # empty tree
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:   # if this node has lchild
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return    # end the loop
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:      # if is duplicate value then do nothing
                return

    def search(self, root, val):
        if not root:
            return root
        elif val < root.data:
            return self.search(root.lchild, val)
        elif val > root.data:
            return self.search(root.rchild, val)
        else:
            return root


    def pre_order(self, root):  # 前序遍历：E,A,C,B,D,G,F,
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):  # 中序遍历：A,B,C,D,E,G,F,
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def back_order(self, root):  # 后序遍历：B,D,C,A,F,G,E,
        if root:
            self.back_order(root.lchild)
            self.back_order(root.rchild)
            print(root.data, end=",")




tree = BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.back_order(tree.root)
result = tree.search(tree.root, 4)
print(result)

# 4,2,1,3,6,5,7,9,8,
# 1,2,3,4,5,6,7,8,9,
# 1,3,2,5,8,9,7,6,4,


