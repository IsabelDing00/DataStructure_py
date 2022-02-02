# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

'''
1. Queue
2. python 里的队列内置模块 -> queue2.py
'''

class Queue:
    def __init__(self, size):
        self.queue = [0 for _ in range(size)]  # create a list with the size
        self.size = size
        self.rear = 0   # the end of queue
        self.front = 0  # the front of queue

    def push(self, element):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is full.")

    def pop(self):    # just move the front to point to the next index, and return
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)
for i in range(4):  # because if the list has 10 boxes then I can only put 9 elements into it.
    q.push(i)

print(q.is_full())




