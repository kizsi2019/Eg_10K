szamok = [1,2,3,4,5,6,7,8,9,10,11,12,13]
parosszamok = []

def paros(szam):
    for szam in szamok:
        if szam % 2 == 0:
            parosszamok.append(szam)
    return(parosszamok)




print(paros(szamok))