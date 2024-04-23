maganhangzok = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']

def maganhangzok_szamolasa(szoveg):
    maganhangzok_szama = 0

    for karakter in szoveg:
        if karakter in maganhangzok:
            maganhangzok_szama += 1
    return maganhangzok_szama

print("Üdvözöllek a magánhangzó meghatározó programban!")

szoveg = input("Add meg a szöveget: ")

maganhangzok_szama = maganhangzok_szamolasa(szoveg)

print(f"A(z) '{szoveg}' szövegben {maganhangzok_szama} magánhangzó található.")