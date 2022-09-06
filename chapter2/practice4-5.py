from timeit import Timer

def foundKn(l, k):
    kmin = []
    num = max(l)
    count = [0]*(num+1)
    for i in range(len(l)):
        count[l[i]] += 1
    s = []
    for i in range(num+1):
        for j in range(count[i]):
            s.append(i)
    return s[k-1]


def foundKnlogn(l, k):
    l.sort()
    return l[k-1]


