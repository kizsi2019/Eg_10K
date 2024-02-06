
nyelvek = ['Python', 'C', 'C++', 'Java']

   
nyelvek.sort()
print(nyelvek)
   
nyelvek.reverse()  
print(nyelvek)


print(nyelvek.index('C'))


print(nyelvek.count('Python'))

   
print('C++' in nyelvek)


nyelvek.append('Python')
    
nyelvek_masolat = nyelvek.copy()
    
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)
    
nyelvek.insert(1, 'Go')     
  

  