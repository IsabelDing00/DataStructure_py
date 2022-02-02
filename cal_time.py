# -*- Coding = utf-8 -*-
# @Author: Isabel Ding
# This is for calculate a code running time

import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s sec." % (func.__name__, t2-t1))
        return result
    return wrapper