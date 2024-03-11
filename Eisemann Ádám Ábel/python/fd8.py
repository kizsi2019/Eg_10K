def atlag_es_indexek(szamok_lista):
    if not szamok_lista:
        return None, []  

    osszeg = sum(szamok_lista) 
    atlag = osszeg / len(szamok_lista)  

    nagyobbak_indexe = [i for i, szam in enumerate(szamok_lista) if szam > atlag]

    return atlag, nagyobbak_indexe

# Példa használat:
szamok_lista = [10, 20, 30, 40, 50]
atlag, nagyobbak_indexe = atlag_es_indexek(szamok_lista)
print("A számok átlaga:", atlag)
print("Az átlagnál nagyobb számok indexei:", nagyobbak_indexe)
