
nyelvek = ['Python', 'C', 'C++', 'Java']
print(nyelvek)

    # sorbarendezi a listát
nyelvek.sort()
print(nyelvek)
    # fordított sorrendbe rendezi a listát
nyelvek.reverse()  
print(nyelvek)


    # az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

    # az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

    # NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)

  
    # a lista végére hozzáfűz egy elemet
nyelvek.append('Python')
    
    # a listát másolja
nyelvek_masolat = nyelvek.copy()
    
    # a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
    
    # adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')     
  