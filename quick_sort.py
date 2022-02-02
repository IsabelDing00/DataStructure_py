# -*- Coding = utf-8 -*-
# @Author: Isabel Ding

def partition(li, left, right):
    tmp = li[left]  # Take the first one
    while left < right:  # make sure there is more than one number in the list, line13
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# print(li)
# partition(li, 0, len(li) - 1)
# print(li)
quick_sort(li, 0, len(li) - 1)
print(li)
