# 1

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def parosszamok(x):
    for i in x:
        if i % 2 == 0:
            print(i)


parosszamok(lista)

# 2


def legnagyobbszam(x):
    print(max(x))


legnagyobbszam(lista)


# 3

szoveg = input("Kérek egy szöveget: ")
szoveglista = szoveg.split()


def szoszamolo(x):
    print(len(x))


szoszamolo(szoveglista)


# 4


def listaszamatlag(x):
    atlag = sum(x) / len(x)
    print(atlag)


listaszamatlag(lista)


# 5

# Ugyanaz, mint az 1. feladat.

# 6


def minmax(x):
    print(max(x) - min(x))


minmax(lista)


# 7

# Ugyanaz, mint a 3. feladat

# 8


def listaszamatlagextravaganza(x):
    atlagextra = sum(x) / len(x)
    print(atlagextra)
    for i in x:
        if i > atlagextra:
            print(i)


listaszamatlagextravaganza(lista)


# 9


def listaforditas(x):
    x.reverse()
    print(x)


listaforditas(lista)
