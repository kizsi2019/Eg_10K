def legkisebb_legnagyobb_kulonbseg(szamlista):
    szamlista.sort()
    legkisebb = szamlista[0]
    legnagyobb = szamlista[-1]
    kulonbseg = legnagyobb - legkisebb
    return kulonbseg

szamok = [10,20,30,50,8,80,70,50]
print("A kulonbseg a legkisebb es a legnagyobb szam kozott a listaban", legkisebb_legnagyobb_kulonbseg(szamok))