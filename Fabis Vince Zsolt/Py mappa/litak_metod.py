nyelvek = ['Python','C','c++']
 # sorbarendezi a listát
nyelvek.sort()

# fordított sorrendbe rendezi a listát
nyelvek.reverse()  
# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)
  