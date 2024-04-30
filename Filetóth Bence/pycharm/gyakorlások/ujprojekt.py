szam1 = 5
szam2 = 10
szam3 = 9



print(szam1 + szam3)

print(szam2>szam3)

print((szam1+szam2+szam3)/3)

print(szam1==szam3)

print(szam1*szam2*szam3)

print(szam2%szam3)


hello = "hello"

nev = input("M a neved?")

print(hello.nev)

for i in range(5):
    print(hello.nev)

for i in range(200):
    if i % 2==0:
        print(i)


if szam2>szam1:
    print(szam2,"nagyobb mint",0, szam1)




if szam1<szam3:
    print(szam1+szam3)





for i in range(501):
    if i % 5==0:
        print(i,"osztható 5-tel")
    else:
        print(i,"nem osztható 5-tel")


for i in range(30, 251):
    if i % 6 ==0:
        print(i)





for i in range(30,251, 6):
    print(i)








allatok = ["lizards", "agamas", "skinks", "geckos", "snakes"]
for i in allatok:
    print(i)
    if i == "agamas":
        break




for i in range(90, 778, 3):
    print(i)
for i in range(90, 778):
    if i % 3==0:
        print(i)

db = 0
for i in range(66,345):
    if i % 11 == 0:
        db += 1
print(db)

osszeg = 0
for i in range(77,100):
    if i % 2 == 0:
        osszeg += 1
        print(i,osszeg)
print(osszeg)


osszeg1 = 0
for i in range(444,526):
    if i % 2 == 0:
        osszeg1 += 1
        print(osszeg1)



hanydb = 0
for i in range(2,334):
    if i % 6 ==0:
        hanydb+=1
print(hanydb)





data = int(input(" adj egy számot"))
hany=0
for i in range(data, 9, -1):
    if i % 9 == 0:
        print(i)
        hany += 1
print(hany)





