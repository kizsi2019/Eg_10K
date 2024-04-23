szamok = [1, 2, 3, 4, 5]
def legnagyobb(x, *args):
    legnagyobb = x
    for szam in args:
        if szam > legnagyobb:
                legnagyobb = szam
        return legnagyobb

print(legnagyobb(szamok))