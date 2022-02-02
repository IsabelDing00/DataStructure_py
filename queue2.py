# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

'''
1. python 里的队列内置模块
'''

# import queue   -> 这个queue是为了保证线程安全的

from collections import deque  # -> 这个里面的deque是双向队列

# queue
# q = deque([3,4,5,6,7], 10)    # if there is more than 10 elements, once I push a new element in,and the first element will be poped out
# q.append(1)  # add 1 at the right end
# q.popleft()  # pop the left one
#
# # deque
# q.appendleft(2) # add at the left end
# q.pop()         # pop at the right end


# to get the last 5 elements from "test.txt"
def tail(num):
    with open("test.txt","r") as f:
        q = deque(f,num)   # check line 10
        return q

for line in tail(5):
    print(line,end = "")
