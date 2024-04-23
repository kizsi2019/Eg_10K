
allat1 = input("Add meg az első állat nevét: ")
allat2 = input("Add meg a második állat nevét: ")
allat3 = input("Add meg a harmadik állat nevét: ")

allatok = [allat1, allat2, allat3]
allatok.sort()

print("Az állatok abc sorrendben:")
for allat in allatok:
    print(allat)