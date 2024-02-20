def atlag(szamok_lista):
    if not szamok_lista:
        return None  

    osszeg = sum(szamok_lista) 
    atlag = osszeg / len(szamok_lista)  

    return atlag  

    
szamok_lista = [10, 20, 30, 40, 50]
eredmeny = atlag(szamok_lista)
print("A számok átlaga:", eredmeny)
