def atlag_es_indexek(szamlista):
    if len(szamlista) == 0:
        return 0, []  
    osszeg = sum(szamlista)
    atlag = osszeg / len(szamlista)
    nagyobbak_indexei = [i for i, szam in enumerate(szamlista) if szam > atlag]
    return atlag, nagyobbak_indexei


szamok = [10, 20, 30, 40, 50]
atlag, indexek = atlag_es_indexek(szamok)
print(f"A számok átlaga: {atlag}")
print(f"Azoknak az indexei, amelyek nagyobbak, mint az átlag: {indexek}")
