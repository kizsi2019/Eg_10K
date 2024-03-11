szavak =[]
szo = input("Adj meg szavakat!")
while szo !='':
    szavak.append(szo)
    szo = input("Adj meg szavakat!")
print(szavak)
legkisebb = szavak[0] 
legnagyobb = szavak[0] 

for szo in szavak:
    if len(szo) < len(legkisebb):
        legkisebb = szo
    if len(szo) > len(legnagyobb):
        legnagyobb = szo

print(f'A legrovidebb szo a listaban:{legkisebb}')
print(f'A leghosszabb szo a listaban:{legnagyobb}')