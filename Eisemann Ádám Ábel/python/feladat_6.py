
def min_max_kulonbseg(szamok):
    min_szam = min(szamok)
    max_szam = max(szamok)
    return max_szam - min_szam

szamok = [1,2,3,4,5,6,7,8,9,10]
print(max(szamok))
print(min(szamok))
print(min_max_kulonbseg(szamok))