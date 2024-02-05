szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
tbetus = []

for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        tbetus.append( szo )
        
print(tbetus)