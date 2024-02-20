
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

valami=[]
for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        valami.append(szo)
print(valami)