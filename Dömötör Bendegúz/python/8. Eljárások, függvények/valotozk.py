import random

kitalalando = random.randint(1, 10)
tippek_szama = 0

def eltalalta(tipp, kitalalando):
    return tipp == kitalalando

def tipp_bekero():
    while True:
        try:
            tipp = int(input("Adj meg egy tippet 1 és 10 között: "))
            if 1 <= tipp <= 10:
                return tipp
            else:
                print("A tippnek 1 és 10 között kell lennie!")
        except ValueError:
            print("Érvénytelen input. Kérlek adj meg egy számot!")

def main():
    global tippek_szama
    print("Üdvözöllek a játékban! Találd ki a számot 1 és 10 között.")

    while True:
        tipp = tipp_bekero()
        tippek_szama += 1

        if eltalalta(tipp, kitalalando):
            print(f"Gratulálok, eltaláltad a számot {kitalalando}-t {tippek_szama} tippelés után!")
            break
        else:
            print("Sajnos nem találtad el, próbáld újra!")

if __name__ == "__main__":
    main()