def fibanoci(a):
    s = 1
    t = 1
    print(s)
    print(t)
    d = 0
    for a in range(1, a-1):
        d = s + t
        print(d)
        s = t
        t = d
fibanoci(5)