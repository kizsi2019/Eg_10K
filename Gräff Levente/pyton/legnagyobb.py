
def legnagyobb_elem(szam):
    legnagyobb=szam[0]
    for elem in szam:
        if elem > legnagyobb:
            legnagyobb = elem
        return legnagyobb
szam=[4,5,2,56,3,5,2,4,]
max_elem=legnagyobb_elem(szam)
print("A legnagyobb szám a", max_elem,)