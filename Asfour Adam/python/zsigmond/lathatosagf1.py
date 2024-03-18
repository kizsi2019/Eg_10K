import random

def eltalalta(tipp, kitalalando):
    return tipp == kitalalando

def tipp_bekero():
    try:
        tipp = int(input("Adja meg a tippjét (1-10): "))
        if 1 <= tipp <= 10:
            return tipp
        else:
            print("A tippnek 1 és 10 között kell lennie!")
            return tipp_bekero()
    except ValueError:
        print("Érvénytelen érték!")
        return tipp_bekero()

def main():
    kitalalando = random.randint(1, 10)
    tippelesek_szama = 0
    eltalalt = False

    while not eltalalt:
        tipp = tipp_bekero()
        tippelesek_szama += 1
        eltalalt = eltalalta(tipp, kitalalando)

        if eltalalt:
            print(f"Gratulálok! A kitalálandó szám {kitalalando} volt, és {tippelesek_szama} próbálkozásból találtad meg.")
        else:
            print("Sajnos nem találtad meg a kitalálandó számot. Próbáld újra!")

if __name__ == "__main__":
    main()