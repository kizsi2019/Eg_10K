szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
T_lista=[]
for szo in szavak:
    if szo[0] == 'T' or szo[0] == 't':
        T_lista.append(szo)

print(T_lista)
