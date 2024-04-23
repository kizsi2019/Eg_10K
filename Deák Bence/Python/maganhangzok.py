szoveg = input("Kérek egy szöveget: ").lower()
maganhangzok = ["a", "á", "e", "é", "u", "ú",
                "ü", "ű", "o", "ó", "ö", "ő", "i", "í"]


def maganhangkereso(x):
    darabszam = 0
    for i in x:
        if i in maganhangzok:
            darabszam += 1
    return f"A szövegben lévő magánhangzók száma: {darabszam}"


print(maganhangkereso(szoveg))
