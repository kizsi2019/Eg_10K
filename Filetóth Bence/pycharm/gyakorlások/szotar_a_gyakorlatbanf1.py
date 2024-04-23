'''polc = []

szerzo = input("Adja meg a szerző nevét: ")
cim = input("Adja meg a könyv címét: ")

polc.append({
    'nev' : szerzo,
    'cím' : cim
})

for kulcs in polc:
    print(kulcs, polc(kulcs))'''


polc = []
while True:
    szerzo = input("Adj egy szerzőt: ")
    if szerzo == "":
        break
    cim = input("Adj egy címet: ")
    polc.append({"szerzo": szerzo, "cím": cim})
print(polc)