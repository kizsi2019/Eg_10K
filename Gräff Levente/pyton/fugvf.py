def osszegzo(x, *args):
    osszeg = 0
    for szam in args:
        osszeg += szam
        return osszeg
print(osszegzo(1,2,3,10,100))



