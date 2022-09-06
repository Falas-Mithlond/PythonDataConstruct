import timeit
import random

for i in range(10000, 1000000, 10000):
    
    x = {j:None for j in range(i)}
    t1 = timeit.Timer("x.get(random.randrange(%d))"%i, "from __main__ import random, x")
    t2 = timeit.Timer("x[random.randrange(%d)] = random.randrange(%d)"%(i,i), "from __main__ import random, x")
    dget_time = t1.timeit(number=1000)
    dint_time = t2.timeit(number=1000)
    print("%d, %10.3f, %10.3f"%(i, dget_time, dint_time))