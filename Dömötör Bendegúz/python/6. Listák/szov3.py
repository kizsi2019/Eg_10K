mondat = input('Adj meg egy mondatot! ')

if mondat[-1] == "?":
    print("A mondatod kérdő mondat!")
if mondat[-1] == ".":
    print("A mondatod kijelentő mondat!")
if mondat[-1] == "!":
    print("A mondatod felkiálltó mondat!")
else:
    print("Nincs irásjel a mondat végén!")