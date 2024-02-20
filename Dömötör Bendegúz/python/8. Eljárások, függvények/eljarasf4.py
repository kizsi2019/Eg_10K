def legrövidebb_szó(szavak):
    legrövidebb = szavak[0]
    for szó in szavak:
        if len(szó) < len(legrövidebb):
            legrövidebb = szó
    return legrövidebb

def main():
    szavak = []
    for i in range(3):
        szó = input(f"Kérem, adjon meg egy szót ({i+1}. szó): ")
        szavak.append(szó)

    legrovidebb_szó = legrövidebb_szó(szavak)
    print(f"A legrövidebb szó: {legrovidebb_szó}")

main()
