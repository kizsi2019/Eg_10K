def legnagyobb_elem(lista):

    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem
    return legnagyobb


lista = [1,2,3,4,5]
max_elem = legnagyobb_elem(lista)
print("A lista legnagyobb eleme:", max_elem)