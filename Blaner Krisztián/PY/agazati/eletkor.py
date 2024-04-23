u = int(input("Kérem az életkorát: "))
if u < 0:
    print("Az életkor nem lehet negatív szám!")
elif u < 18:
    print("Ön még kiskorú.")
elif u < 60:
    print("Ön felnőtt korú.")
elif u >= 60:
    print("Ön idős korú")
else:
    print("Valami hiba történt.")