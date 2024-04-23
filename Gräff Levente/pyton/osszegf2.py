szamok=[]
osszeg=0

szam= int(input("adj szamot"))

while(-5 <= szam <=5):
    szamok.append(szam)
    osszeg+= szam
    szam=int(input("adj szamt"))
print(f"a lista: {szamok}")
print (f"az összegük:{osszeg}")

