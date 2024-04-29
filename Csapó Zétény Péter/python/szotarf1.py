nev = input("Add meg a kutya nevét")
fajta = input("Adja meg a kutya faját")
Eletkor = input("Add meg a kutya életkorát")
Oltas = input("Rendelkezik oltással? [True,false")
Kutya = {
    'nev': nev,
    'fajta': fajta,
    'eletkor': Eletkor,
    'oltas': True
}

for kulcs in Kutya:
    print(kulcs, Kutya[kulcs])
