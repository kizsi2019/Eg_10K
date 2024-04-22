lista = [1,2,3,4,5,6]
def paros_e(lista):
    for elem in lista:
        if elem % 2 == 0:
            return True
        
    return False
            
print(paros_e(lista)) 