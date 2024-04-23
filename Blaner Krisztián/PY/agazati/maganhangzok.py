u = input("Adjon meg egy szöveget:")
def maganhangzoszamlalo(szoveg:str):
    x = 0
    for i in szoveg:
        if i.lower() in "öüóeuioőúaéáűí":
            x +=1
    return x

print(f"A szövegben {maganhangzoszamlalo(u)} magánhangzó található" )