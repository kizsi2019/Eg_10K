nev = input("Add meg a kutya nevét")
fajta = input("Add meg a kutya fajtajat")
eletkor = input("add meg a a kutya eletkorat")
oltas = input("Rendelkezik oltassal?[true/false]")
kutya = {
    'nev' : nev,
    'fajta' : fajta,
    'eletkor' : eletkor,
    'oltas' : oltas, 
}
for kulcs in kutya:
    print(kulcs, kutya[kulcs])