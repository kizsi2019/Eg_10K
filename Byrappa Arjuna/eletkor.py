kor = int(input("add meg korod"))

if kor < 0:
    print("negativ nem lehet")
if kor == 0:
    print("újszülött")
if kor < 18 and kor > 0:
    print("még kiskorú")
if kor > 18 and kor <= 32:
    print("felnőtt korú")

if kor >= 65:
    print("idős korú")