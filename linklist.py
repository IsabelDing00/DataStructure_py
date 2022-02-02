# -*- Coding = utf-8 -*-
# @Author: Isabel Ding


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        p = self.head
        count = 1
        print(count)
        while p != None:  # when p is not none
            count += 1
            p = p.next
        return count

    def travel(self):
        p = self.head
        while p != None:
            print(p.item, end = " ")
            p = p.next
        print(" ")

    def add(self, element):  # add a element at head
        node = Node(element)
        node.next = self.head   # this step goes first because we use head to travel the linklist
        self.head = node

    def append(self,element):  # add a element at tail
        node = Node(element)
        if self.is_empty():
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def insert(self, element, pos):  # pos position start from 0
        if pos <= 0:
            self.add(element)
        elif pos > self.length() - 1:
            self.append(element)
        else:
            pre = self.head
            node = Node(element)
            while pos - 1:
                pre = pre.next
                pos -= 1
            # when we finish while loop, pre points to pos-1
            node.next = pre.next
            pre.next = node

    def search(self,element):
        p = self.head
        while p:
            if p.item == element:
                return True
            else:
                p = p.next
        return False

    def remove(self,element):
        cur = self.head
        pre = None
        while cur:
            if cur.item == element:
                # if this element is the head
                if cur ==  self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                break       # finish the after we remove this element
            else:
                pre = cur
                cur = cur.next



if __name__ == "__main__":
    ll = Linklist()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)  # 8 1 2 3 4 5 6

    ll.insert(100,3)
    ll.insert(101,9)  # 8 1 2 100 3 4 5 6 101
    ll.travel()

    ll.remove(100)
    ll.travel()     # 8 1 2 3 4 5 6 101


# def create_linklist_head(li):
#     head = Node(li[0])
#     for element in li[1:]:   # because the first element is the head of linklist already
#         node = Node(element) # create a new node
#         node.next = head
#         head = node
#     return head
#
# def create_linklist_tail(li):
#     head = Node(li[0])
#     tail = head
#     for element in li[1:]:
#         node = Node(element)  # create a new node
#         tail.next = node      # this node.next point to tail
#         tail = node
#     return head
#
# def print_linklist(li):
#     while li:    # when the item.next is not None
#         print(li.item, end=",")
#         li = li.next
#
# # lk = create_linklist_head([1,2,3,4,6,8])
# # print_linklist(lk) # 8,6,4,3,2,1,
#
# lk = create_linklist_tail([1,2,3,4,6,8])
# print_linklist(lk)  # 1,2,3,4,6,8,
