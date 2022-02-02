# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

'''
<--  这个是这次下面用到的一些语法  -->
1。
not与逻辑判断句if连用，代表not后面的表达式为False的时候，执行冒号后面的语句。比如：
a = False
if not a:   (这里因为a是False，所以not a就是True)
    print "hello"
这里就能够输出结果hello

a = None同理
————————————————
版权声明：本文为CSDN博主「Talon_z」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_37843198/article/details/78890523

2。https://blog.csdn.net/CLHugh/article/details/75000104 这个是有关python class的文章
3. https://zhuanlan.zhihu.com/p/84327339   article about HashTable

'''
class LinkList:
    class Node:
        def __init__(self, item = None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node
        def __next__(self):
            if self.node:   # 如果node不是空， 保存这个node
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        def __iter__(self):
            return self

    def __init__(self, iterable = None):  # init for class LinkList,  iterable is a list
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, element):   # add an element at the tail
        s = LinkList.Node(element)
        if not self.head:    # 当是遍历一个空链表时，if not self.head:为True， check this link:https://zhaochj.github.io/2016/05/12/2016-05-12-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E9%93%BE%E8%A1%A8/
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for element in iterable:
            self.append(element)

    def find(self, element):
        for n in self:
            if n == element:
                return True
        else:          # if the element is not in the linklist then return false
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):    # to print the linklist elements as string
        return "<<"+", ".join(map(str,self)) +">>"

# lk = LinkList([1,2,3,4,5])
# for element in lk:
#     print(element)   # 1 \n 2 3 4 5
#
# print(lk)   #<<1, 2, 3, 4, 5>>

class HashTable:
    def __init__(self, size = 101):
        self.size = size            #  我们将数组总长度设为模数，将key值直接对其取模，所得的值为数组下标。
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def insert(self,k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)

print(",".join(map(str,ht.T)))   # <<0>>,<<1, 102>>,<<>>,<<3>>,<<>>,<<>>
print(ht.find(2))