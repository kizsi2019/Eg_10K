def atlag_es_indexek(szamlista):
    osszeg = 0
    for szam in szamlista:
        osszeg += szam
    atlag = osszeg / len(szamlista)
    
    nagyobbak_indexei = []
    for i in range(len(szamlista)):
        if szamlista[i] > atlag:
            nagyobbak_indexei.append(i)
    

szamlista = [123131231, 131514123,1312313]
atlag, nagyobbak_indexei = atlag_es_indexek(szamlista)
print("A számok átlaga:", atlag)
print("Azok a szamok amik nagyobbak:", nagyobbak_indexei)
