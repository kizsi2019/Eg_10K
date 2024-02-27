def kulonbseg(szamok_lista):
    if not szamlista:
        return None  

    legkisebb = min(szamlista) 
    legnagyobb = max(szamlista)  

    kulonbseg = legnagyobb - legkisebb  

    return kulonbseg  


szamlista = [10, 5, 20, 8, 15]
eredmeny = kulonbseg(szamlista)
print("A legkisebb és legnagyobb szám közötti különbség:", eredmeny)
