import timeit


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = []
    l = [i for i in range(1000)]


def test4():
    l = []
    l = list(range(1000))


t1 = timeit.Timer("test1()", setup="from __main__ import test1")
t2 = timeit.Timer("test2()", setup="from __main__ import test2")
t3 = timeit.Timer("test3()", setup="from __main__ import test3")
t4 = timeit.Timer("test4()", setup="from __main__ import test4")

print(t1.timeit(number=10000))
print(t2.timeit(number=10000))
print(t3.timeit(number=10000))
print(t4.timeit(number=10000))
