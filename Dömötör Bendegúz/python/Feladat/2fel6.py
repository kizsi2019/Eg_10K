import random

def minmax_kulonbseg(lista):
    legkisebb = min(lista)
    legnagyobb = max(lista)
    return legnagyobb - legkisebb

randomszamok = [1,2,3,4,5,6,7]
print(minmax_kulonbseg(randomszamok))