lista = []

while True:
    szam = input("Adjál meg egy egész számot")
    szam = int(szam)
    def ketto_oszthato(lista):
        darab = 0
        for elem in lista:
            if elem % 2 == 0:
                print("Összes páros szám: " )
                lista.append(int(szam))
                if szam == ' ':
                    break