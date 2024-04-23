kor = int(input("Kérem adja meg az életkorát: "))
if kor <= 0:
    print("Az életkor nem lehet negatív szám, sem 0!")
elif kor <= 17:
    print("Ön még kiskoru")
elif kor < 65:
    print("Ön felnőtt")
else:
    kor > 65
    print("Ön idős korú")

