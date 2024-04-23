beker = []

for i in range(3):
    beker_szo = input("Adjál meg egy egész szót")
    beker.append(beker_szo)
def szavak(beker):
    min = beker[0]
    for szo in beker:
        if len(szo) < len(min):
            min = szo
    print(f"A legrövidebb szo: {min}")
szavak(beker)


















