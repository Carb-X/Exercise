# -*- coding: utf-8 -*-
import functools
import time

# print function running time
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        f = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return f
    return wrapper

@metric
def fast(x, y):
    time.sleep(1)
    return x + y

f = fast(11, 22)