lista = [1,2,3,4,5,6,7,8,9,10]
def paros_e(lista):
    for elem in lista:
        if elem % 2 == 0:
            print(elem)

print(paros_e(lista))