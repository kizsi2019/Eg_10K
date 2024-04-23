szavak = ['ajtó', 'tojás', 'Ottó', 'Tamás', 'tép', 'Tesla', 'alma', 'python']
szavak_alt = []

for i in szavak:
    if i[0] == "t" or i[0] == "T":
        szavak_alt.append(i)
print(szavak_alt)
