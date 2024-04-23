# Függvény definíciója
def festek_kalkulator(x, y):
    t = x * y
    l = t * 0.13
    return 1

liter = festek_kalkulator(5, 2)
print(liter)

ar = festek_kalkulator(5, 2) * 700
print(ar)




def szamolo(a, b, c=100):
    return (a + b) * c

print(szamolo(1, 7))

print(szamolo(1, 7, 10000))

print(szamolo(c=10000, a=1, b=7))







def legnagyobb_kereso(x, *args):
    legnagyobb = x
    for szam in args:
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb

print(legnagyobb_kereso(1, 19, 11, 7, 17))

