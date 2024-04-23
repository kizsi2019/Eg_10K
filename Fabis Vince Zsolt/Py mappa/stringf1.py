mondat = input("Adj meg egy mondtatot!")
if mondat[-1] == '?':
    print("Ez a mondat kérdő mondat")
elif mondat[-1] == '.':
    print("Ez kijelentő mondat")
else:
    print("Ez felkiáltó / felszólító / óhajtó mondat")
