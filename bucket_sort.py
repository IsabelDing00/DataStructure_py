# -*- Coding = utf-8 -*
# @Author: Isabel Ding
# If there is a long list with unsorted numbers, compare to count_sort
# 桶排序：首先将元素分在不同的桶中， 在对每个桶的元素排序


def bucket_sort(li, n=100, max_num=10000):  # 100 buckets, and the max number is 10000
    buckets = [[] for _ in range(n)]   # create buckets,二维的列表，每个列表是个桶，每个桶里有数
    for var in li:
        i = min(var // (max_num//n), n-1)  # i means which bucket the var should go. Notice: if i=10000, then the bucket should be 100 (max_num//n), but we only have 0-99 (0,n-1), so we use min( ?,n-1) to limit the number of the bucket
        buckets[i].append(var)   # append the var into the bucket
        # keep the order of the bucket, bubble sort method
        for j in range(len(buckets[i])-1, 0, -1):     # range() 后不包，所以从bucket最后一个元素朝前算，算到正数第二个但应该写0
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
            else:
                break
    sorted_li=[]
    for bucket in buckets:
        sorted_li.extend(bucket)
    return sorted_li

import random
li = [random.randint(0,10000) for i in range(10000)]

li = bucket_sort(li)
print(li)



