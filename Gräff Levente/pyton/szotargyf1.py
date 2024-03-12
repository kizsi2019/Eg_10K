
polc = []
while True:
    szerzo = input("Kérem a könyv szerzőjét: ")
    if not szerzo:
        break
    
    cim = input("Kérem a könyv címét: ")

    polc.append({
        'szerzo': szerzo,
        'cim': cim
    })

print(polc)