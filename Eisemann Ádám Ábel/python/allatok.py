elso = str(input("Add meg az első állat nevét: "))
masodik = str(input("Add meg az masodik állat nevét: "))
harmadik = str(input("Add meg az harmadik állat nevét: "))

allatok = [elso, masodik, harmadik]
allatok.sort()
print(f'Az állatok abc sorrendbe:{allatok} ')
for allat in allatok:
   print(allat)
