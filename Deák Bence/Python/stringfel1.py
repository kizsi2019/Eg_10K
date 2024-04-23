mondat = input("Írj egy szép mondatot UwU: ")

if mondat[-1] == ".":
    print("A mondat kijelentő jellegű.")
elif mondat[-1] == "?":
    print("A mondat kérdő jellegű.")
elif mondat[-1] == "!":
    print("A mondat felkiáltó jellegű.")
else:
    print("A felhasználó enyhén retard.")
