# -*- Coding = utf-8 -*-
# @Author: Isabel Ding


'''
Find the way to get out from the maze, 1 means wall, not accessable
1. Stack - 深度优先搜索
2. Queue - 广度优先搜索
'''

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

dirs = [                   # x：横坐标， y：纵坐标
    lambda x,y: (x+1, y),  # up
    lambda x,y: (x-1, y),  # down
    lambda x,y: (x, y-1), # left
    lambda x,y: (x, y+1) # right
]

def maze_path(x1,y1,x2,y2):     # x1,y1: the point to begin, x2, y2: the point to exit
    stack= []
    stack.append((x1, y1))      # all the point location will be showed as tuple
    while (len(stack)) > 0:     # if the stack is empty, then there is no way to find the path from beginning to end
        curNode = stack[-1]     # top of stack
        if curNode[0] == x2 and curNode[1] == y2:
            # reach to the end
            for p in stack:
                print(p)
            return True

        # 4 directions
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])  # next node is a tuple as will, (curNode[0], curNode[1])
            # check if next node is 0
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 2 表示已经走过
                break   # 只要我能找到一个可以走的点就可以了
        else:   # 如果一个都找不到
            maze[nextNode[0]][nextNode[1]] = 2      # 如果四面都不能走, 这里用nextnode 是因为根据上一个for循环，此刻的这个位置已经是nextnod，那么要把此刻的位置标记为2
            stack.pop()
    else:
        print("There is no way")
        return False

maze_path(1,1,8,8)
