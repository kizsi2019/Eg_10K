lista = []
for i in range(3):
    bekert_szo = input("Adj meg egy szot")
    lista.append(bekert_szo)  
 
def szohossz(lista):
   min = lista[0]
   for szo in lista:
      if len(szo) < len(min):
        min = szo
   print("a legrovidebb szo: {min}")

szohossz(lista) 