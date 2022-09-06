from timeit import Timer
import random

for i in range(1000000, 10000000, 100000):
    t = Timer("del x[random.randrange(%d)]"%i, "from __main__ import random, x")

    x = list(range(i))
    lst_time = t.timeit(number = 1)
    x = {j:None for j in range(i)}
    dic_time = t.timeit(number=1)
    
    print("%d, %10.3f, %10.3f"%(i, lst_time*10000, dic_time*10000))