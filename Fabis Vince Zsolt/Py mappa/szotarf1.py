nev = input("Add meg a nevét:")
fajta = input("Add meg a kutya fajtáját:")
eletkor = input("Add meg a kutya életkorát:")
oltas = input("Renselkezik oltással? [True,False]")
kutya = {
    'nev': nev,
    'fajta': fajta,
    'eletkor': eletkor,
    'oltas': oltas

    }
for kulcs in kutya:
    print(kulcs, kutya[kulcs])