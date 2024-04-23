kor = int(input("Kérem az életkorát: "))
if kor < 0:
    print("A szám nem lehet negatív.")
elif kor > -1 and kor < 18:
    print("Ön még kiskorú.")
elif kor > 18 and kor < 60:
    print("Ön felnőtt korú.")
else:
    print("Ön idős korú.")
