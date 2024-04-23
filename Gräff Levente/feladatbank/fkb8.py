#8. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja a listában található számok átlagát, és azok közül azoknak az indexeit, amelyek nagyobbak, mint az átlag.
szamok=[1,2,3,5,2,1,6,8,6,5,4,4,6,8]
def atlag_index(szamok):
    atlag=sum(szamok)/len(szamok)
    for i in range(len(szamok)):
        if szamok[i]>atlag:
            print(i)
atlag_index(szamok)