maganhangzo_lista = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
maglist = []
magliststr = ""
def maganhangzo(betu):
    if betu.lower() in maganhangzo_lista:
        return 1
    else:
        return 0
    
def maganhangzo_szama(szoveg):
    n = 0
    for i in (szoveg):
        if maganhangzo(i):
            n = n + 1
            maglist.append(i)
            magliststr.join(i)
    return n

bemeno_szoveg = input("Adjon meg egy szöveget: ")
print(f"A szövegben {maganhangzo_szama(bemeno_szoveg)} magánhangzó található.\n Magánhangzók: {maglist} \n {magliststr}")