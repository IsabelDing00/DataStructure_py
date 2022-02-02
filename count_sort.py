# -*- Coding = utf-8 -*-
# @Author: Isabel Ding
#计数算法,但是limit是这个算法的n如果很大就会需要更多的空间
'''
a list has numbers range from 0-100, but we don't know the length of the list, design a count_sort with
time complexity = O(n), sort the list

if -> list1 = [1,3,2,4,1,2,3,1,3,5,7]  , for easy way to see the result, I changed the max_count to 10
after enumerate(count)
print(ind,val) will be:
0 0
1 3    has 3 1s
2 2
3 3
4 1
5 1
6 0
7 1
and then I got the final result as [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 7]
'''
import copy

from cal_time import *

@cal_time
def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]   # create a list with length is (max_count+1)
    for val in li:        # 0(n)
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):   # if the val is 0, then the number will not be appended into the list
            li.append(ind)       # O(n)

# import random
# li = [random.randint(0,100) for _ in range(1000)]
# print(li)
# count_sort(li)
# print(li)
#
# list1 = [1,3,2,4,1,2,3,1,3,5,7]
# count_sort(list1)
# print(list1)

@cal_time
def sys_sort(li):
    li.sort()

import random
li = [random.randint(0,100) for _ in range(1000000)]

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

count_sort(li)       # count_sort running time: 0.1433260440826416 sec.
sys_sort(li2)        # sys_sort running time: 0.10875415802001953 sec.

# enumerate() example
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
    print(i, element)


