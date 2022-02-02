# -*- Coding = utf-8 -*
# @Author: Isabel Ding
# Radix_sort: sort the list based on the every elements' last digit by using bucket sort method, and then sort the list again based on the last second digit, until we have done the max number's first digit

def radix_sort(li):
    max_num = max(li)  # max_num: 9->1 (only need 1 round), 99->2 (2 rounds), 10000->5
    it = 0    # this is my iterator
    while 10 ** it <= max_num:   # check how many digits max_number has, if the max_num is 9, then our it should be 1
        # create the buckets, 10 buckets, from 0-9
        buckets = [[] for _ in range(10)]
        for var in li:
            # 987: take the 10s ->8: it=1 987//10 = 98, 98%10 = 8
            # 987: take the 100s->9: it=2 987//100 = 9,  9%10 = 9
            digit = (var//10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        # rewrite the li
        it +=1

import random
li = list(range(100000))
random.shuffle(li)
radix_sort(li)
print(li)