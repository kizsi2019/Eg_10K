dolog = input("Adjon meg egy mondatot!")
Szoveg = [dolog]
maganhangzo = ("a","á","e","é","i","í","u","ú","ü","ű","o","ó","ö","ő")
szamlalo=0
if maganhangzo in dolog:
    szamlalo += 1
print(f'A szövegben enny magánhangzó van:', szamlalo)