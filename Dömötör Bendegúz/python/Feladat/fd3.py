def szovegszamlalo(szoveg):
     szavak = szoveg.split()
     return len(szavak)

szoveg = ("Adam egy bombazo retardalt.")
print(szovegszamlalo(szoveg))