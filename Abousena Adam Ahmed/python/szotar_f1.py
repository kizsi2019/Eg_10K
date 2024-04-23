nev = input("Add meg a kutya nevét")
fajta = input("Add meg a kutya fajtáját")
eletkor = input("Add meg a kutya életkorát")
oltas = input("Rendelkezik oltással? [true,false]")
kutya = {
    "nev": 'Bodri',
    "eletkor": 'kutya_eletkor',
    "fajta": 1,
    'oltas': True
}

for kulcs in kutya:
    print(kulcs, kutya[kulcs])