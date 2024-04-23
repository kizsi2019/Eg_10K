

def maganhangzok_szama(szoveg):
    maganhangzok = "aeiuoAIOEU"
    szamlalo = 0
    for karakter in szoveg:
        if karakter in maganhangzok:
            szamlalo += 1
    return szamlalo

szoveg = input("adjon meg egy szoveget")
maganhangzok_szam = maganhangzok_szama(szoveg)
print("A szovegben talalható maganhangzók szama:", maganhangzok_szam)