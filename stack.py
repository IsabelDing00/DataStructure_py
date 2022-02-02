# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

'''
1. For stack
2. brace_match() is for check if the [](){} order matching. For example {[()]}
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())

def brace_match(s):
    match = {"}":"{", "]":"[",")":"("}
    stack = Stack()
    for ch in s:
        if ch in {"(", "{","["}:   # if ch is ( or { or [ 左扩号，then append ch into stack
            stack.push(ch)
        else:    # if ch in {")", "}", "]"}， ch是右括号
            if stack.is_empty():  # 如果stack是空的， 那么报错
                return False
            elif stack.get_top() == match[ch]: # check if the top element in stack is match ch. 看stack的top element是否和右括号match
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:return False

print(brace_match('[{()}(){()}[]({}){}]'))



