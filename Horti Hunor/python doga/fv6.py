def kulonbseg_legkisebb_legnagyobb(szamlista):
    if not szamlista:
        return None

    legkisebb = min(szamlista)
    legnagyobb = max(szamlista)
    kulonbseg = legnagyobb - legkisebb
    return kulonbseg

szamlista = [1,100000]
print("A legkisebb és legnagyobb szám közötti különbség:", kulonbseg_legkisebb_legnagyobb(szamlista))
