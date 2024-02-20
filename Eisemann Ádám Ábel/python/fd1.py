def paros_szamok(lista):

    parosak = []  

    for szam in lista:
        
        if szam % 2 == 0:
           
            parosak.append(szam)

    return parosak  


szamlista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,22,23,25,26,27,29]
eredmeny = paros_szamok(szamlista)
print("Páros számok:", eredmeny)