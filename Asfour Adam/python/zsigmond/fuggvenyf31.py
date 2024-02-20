lista =[1,2,3,4,5,6,7,8,9,10,11,12]

def harommal_oszthatok(lista):
    darab= 0
    for elem in lista:
        if elem % 3 == 0:
            darab += 1
    return darab

print(harommal_oszthatok(lista))