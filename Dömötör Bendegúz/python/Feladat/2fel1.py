szamok = [1,2,4,9,6,1,34,12,1]
parosszamok = []

def paros(szam):
    for szam in szamok:
        if szam % 2 == 0:
            parosszamok.append(szam)
    return(parosszamok)
    
print(paros(szamok))

