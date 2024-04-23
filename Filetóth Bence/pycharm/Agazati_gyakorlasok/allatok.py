allatkert = []
allat1 = input("Kérem az első állatot: ")
allat2 = input("Kérem a második állatot: ")
allat3 = input("Kérem a harmadik állatot: ")

allatkert = [allat1, allat2, allat3]
allatkert.sort()

print("Az állatok ábécé sorrendbe: ")
for allat in allatkert:
    print(allat)