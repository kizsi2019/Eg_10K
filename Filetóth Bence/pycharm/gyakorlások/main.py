import random
#műveletek
x = 40
y = 20
print(x*y)
print(x/y)
print(x//y)
print(x % y)
print(x % 2 == 0)

#logikai

print(x > y)
print(y == x)
print(x >=y )
print(x <= y)

#listák

en_lista = []
print(en_lista)

en_lista = ["tiger", "lion", "eagle", "bearded dragon"]
print(en_lista)
'''for i in en_lista:
    print(en_lista[i])'''

print(len(en_lista))
en_lista.insert(2, "python")
#en_lista[2] = "python"

en_lista.append("pig")
more_list = ["donkey", "bee", "wasp"]
en_lista.extend(more_list)
print(en_lista)

en_lista.remove("wasp")
print(en_lista)

'''en_lista.pop(3)
print(en_lista)
en_lista.pop() #deleteli a lista tartalmát
print (en_lista)

en_lista.clear()
print(en_lista)

del en_lista #deleting the list'''

if "wasp" in en_lista:
    print("benne van a duruzs")
else:
    print("no wasp?")

#Bonyibb műveletek

a = 33
b = 100
if b > a:
    print("100 nagyobb mint 33")

if b == a:
    print("valamit")
elif a < b:
    print("elif feltétel teljesül")

if b == a:
    print("b==a nem teljesül")
elif a > b:
    print("a > b nem teljesül")
else:
    print("else akkor teljesül ha se az if és az elif sem igaz")

#ciklus

for i in range(0, 10):
    print(i)
#nagy lépésekkel
for i in range(0, 21, 2):
    print(i)

#páros vagy nem páros ez itt a kérdés
for i in range(1, 31):
    if i % 2 == 0:
        print(i, "páros")
    else: print(i, "páratlan")


#rand(om): egy random gnerált szám ami 0 és 100 között van
rand = random.randint(0, 100)
print("random", rand)

#5db random szám generálása
random_list = []
for i in range(0, 5):
    rand1 = random.randint(0, 100)
    random_list.append(rand1)
print(random_list)

#mi fogunk definiálni egy függ(öny)vényt
#def kulcsszót fogjuk használni
#Zárójelek között megadjuk mlyen adatokat kap meg a fv
#random.randit(0, 100) random 2 adatot kap itt meg,a tól és az ig-et
#def -> létrehozunk egy új fv, melyikNagyobb!
#itt a bemenet, így fog kinézni 3, 4, 5
valami = input("kérek 3 számot vesszővel elválasztva")
szamok = valami.split(",")
print(szamok)


# a fv célja, hogy eldöntse melyik szám a nagyobb
def melyikNagyobb(lista):
    a = 0
    if int(lista[0]) > int(lista[1]) and int(lista[0]) > int(lista[2]):
        a = int(lista[0])
    elif int(lista[1]) > int(lista[0]) and int(lista[1]) > int(lista[2]):
        a = int(lista[1])
    else:
        a = int(lista[2])
    return a
#return a fv visszatérési érték köznapi eredménye
melyik = melyikNagyobb(szamok)
print(melyik, "szam volt a legnagyobb")