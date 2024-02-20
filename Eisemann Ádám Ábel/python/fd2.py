
def legnagyobb_kereso(szam, lista):
             
    legnagyobb = szam
    for szam in lista:
        if szam > legnagyobb:
                          legnagyobb = szam
    return legnagyobb
    
    
print(legnagyobb_kereso(1, 19, 11, 7, 17))

