nev = input("Adjmeg egy nevet: ")
faj = input("Mia kutya fajtája: ")
eletkor = input("Add meg a kutya életkorát: ")
oltas = input("Oltva van-e a kutya: ")
kutya: dict= {
    'neve': nev,
    'faj': faj,
    'eletkor': eletkor,
    'oltas': oltas
}

for kulcs in kutya:
    print(kulcs, kutya[kulcs])