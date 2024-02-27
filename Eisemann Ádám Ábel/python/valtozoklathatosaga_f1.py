

import random

kitalalando = random.randint(1, 10)
tippek_szama = 0

def eltalalta(tipp, kitalalando):
    if tipp == kitalalando:
        return True
    else:
        return False

def tipp_bekero():
    tipp = int(input("Tippelj! "))
    return tipp

def main():
    tippek_szama = 0
    print("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni!")
    while True:
        tippek_szama += 1
        tipp = tipp_bekero()
        if eltalalta(tipp, kitalalando):
            print(f'Gratulálok, eltaláltad {tippek_szama} próbálkozásból!')
            print("jaték vége!")
            break
main()