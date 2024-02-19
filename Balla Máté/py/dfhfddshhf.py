szam1 = 5
szam2 = 10
szam3 = 9

hello= "hello"

nev = input("mi a neve?")
print(hello,nev)

for i in range(5):
    print(hello,nev)

print("_________________")

for i in range(200):
    if i %2 ==0:
        print(i)

print("_________________")

for i in range(0,200,2):
    print(i)


print("_________________")

if szam2 >= szam1:
    print(szam2,"nagyobb mint", szam1)

print("_________________")

 
for i in range(501):
    if i % 5 ==0:
        print(i)
    else:
        print("nem osztható öttel")
