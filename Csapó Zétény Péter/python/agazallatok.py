allat1 = input("Adja meg az első állat nevét")
allat2 = input("Adja meg a második llat nevét")
allat3 = input("Adja meg a harmadik állat nevét")

allatok = [allat1, allat2, allat3]
allatok.sort()

print("Az állatok ábécé sorredben: ")
for allat in allatok:
    print(allat)