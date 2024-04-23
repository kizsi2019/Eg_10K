konyv = []
while True:
    szerzo = input("Add meg a szerző nevét(nyomj entert a kilépéshez): ")
    if not szerzo:
        break
cim = input("Add meg a könyv címét: ")
konyv.append({"szerzo": szerzo, "cím":cim})

print(konyv)