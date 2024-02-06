szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
tlista=[]

for szo in szavak:
    if szo[0] == 'T' or  szo[0] == 't':
        tlista.append(szo)
print(tlista)