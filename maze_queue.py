# -*- Coding = utf-8 -*-
# @Author: Isabel Ding


'''
Find the way to get out from the maze, 1 means wall, not accessable
1. Stack - 深度优先搜索
2. Queue - 广度优先搜索

Queue

   1 ｜     12 ｜—— 16                           1st layer:1    2nd: 2    3rd:3   4th:4,5    5th:6,7  6th:8, 9, 10
   2 ｜      9 ｜         ｜ 15                  7th:11 ,12, 13           8th:14,15, 16      9th(last): 17
   3 ｜—— 4 —— 6 —— 8 —— 11                      Every time popout the father node(curNode) save the nextNode with its index
   5 ｜                   ｜ 14                 So:   Point:  1  2  3  4  5  6  7  8  9  10  11
   7 ｜—— 10 —— 13        ｜ 17                    PreIndex: -1  0  1  2  2  3  4  5  5   6   8
           if we start from 1, and the end is at 10, then:   ｜--｜-｜----｜-----｜--------｜  （7's index is 6)
'''

from collections import deque

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [  # x：横坐标， y：纵坐标
    lambda x, y: (x+1,y),  # up
    lambda x, y: (x-1,y),  # down
    lambda x, y: (x,y-1),  # left
    lambda x, y: (x,y+1)  # right
]

def print_r(path):
    curNode = path[-1]   # if we reach to the end, the last element is the end point
    realpath = []
    while curNode[2] != -1:  # Save the elements from path into realpath, until the start point(index is -1)
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode[0:2])  # save the start point in realpath, but this will be start from end point to start
    realpath.reverse()

    for node in realpath:
        print(node)


# every time pop out the current node and save the next node in the list -> line
def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))  # 这个可以理解建立一个 3-D list: x, y, and index
    path = []

    while len(queue) > 0:  # queue is not empty
        curNode = queue.pop()  # first one in list and pop it
        path.append(curNode)
        # check if we reach to the end
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        # Save curNode, which will be the last element of path -> line
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])  # check if this node is accessable
            print(path)
            if maze[nextNode[0]][nextNode[1]] == 0:
                print(dir)
                print(nextNode)
                print(maze[nextNode[0]][nextNode[1]])
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # nextNode is the child node of curNode, so save index of curNode
                maze[nextNode[0]][nextNode[1]] = 2  # mark as passed
    else: # there is no path
        print("no path.")
        return False


maze_path_queue(1,1,8,8)