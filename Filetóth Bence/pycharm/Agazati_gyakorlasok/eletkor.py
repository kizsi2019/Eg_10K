
'''szam = int(input("Adja meg az életkorát: "))

if szam >= 1 and szam < 18:
        print("ön még kiskorú.")
elif szam >= 65:
        print("Őn idős korú.")
elif szam >= 18 and szam < 65:
        print("Ön felnőtt korú")
else:
        print("Az életkor nem lehet nulla és negatív szám!")'''



def elojel(szam):
    if szam >= 1 and szam < 18:
        return "ön még kiskorú."
    elif szam >= 65:
        return "Őn idős korú."
    elif szam >= 18 and szam < 65:
        return "Ön felnőtt korú"
    else:
        return "Az életkor nem lehet nulla és negatív szám!"
    
eletkor = int(input("Adja meg az életkorát: "))
print(elojel(eletkor))