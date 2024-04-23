
lista = [123,456,789,234,546,777,973,432]
def legnagyobb_elem(lista):
    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem
    return legnagyobb

max_elem = legnagyobb_elem(lista)
print("A lista legnagyobb eleme:", max_elem)