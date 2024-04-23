animal_names = []

u = input("add meg az első állat nevét: ")
animal_names.append(u)
u = input("add meg a második állat nevét: ")
animal_names.append(u)
u = input("add meg a harmadik állat nevét: ")
animal_names.append(u)

animal_names.sort()
print(f"Az állatok ábécé sorrendben {animal_names}")