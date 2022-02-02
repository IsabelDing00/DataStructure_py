# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

'''
模拟文件系统
FileSystemTree
'''

class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type    # end as "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):     # to print the file name
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name ends with "/"
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self,name):
        if name[-1] != "/":     # ends with "/"
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return        # ends at here, no need to continue
        raise ValueError("Invalid direction.")



tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
# print(tree.root.children)  #  [var/]
# print(tree.ls())     #[var/, bin/, usr/]
tree.cd("bin/")
tree.mkdir("python/")
# print(tree.ls())     # [python/]

tree.cd("../")
print(tree.ls())   # [var/, bin/, usr/]