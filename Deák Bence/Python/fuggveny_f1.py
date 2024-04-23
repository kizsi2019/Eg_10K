def osszegzo(x, *args):
    osszeg = x
    for i in args:
        osszeg += i
    return osszeg


print(osszegzo(1, 2, 3, 1, 1, 100))
