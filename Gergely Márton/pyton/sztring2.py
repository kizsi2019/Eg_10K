mondat = input("Adj meg egy mondatot!")
if mondat[-1] == '?':
    print("Ez egy kérdő mondat")
elif mondat[-1] == '.':
    print("Ez kijelentő mondat")
else:
    print("Ez felkialtó/felszólító/óhajtó mondat")