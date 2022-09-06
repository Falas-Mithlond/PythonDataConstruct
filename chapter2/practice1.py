from timeit import Timer

sorttest = Timer("x.sort()", "from __main__ import x")

for i in range(10000, 1000000, 20000):
    x = list(range(i))
    lst_sort = sorttest.timeit(number=1000)
    print("%d, %10.5f"%(i, lst_sort))