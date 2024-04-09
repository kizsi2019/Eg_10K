homersekletek = []
      
pentek = [11, 19, 17]
szombat = [13, 22, 20]
vasarnap = [15, 30, 25]
hetfo = [7, 16, 15]
      
homersekletek.append(pentek)
homersekletek.append(szombat)
homersekletek.append(vasarnap)
homersekletek.append(hetfo)  
    

[[11, 19, 17], [13, 22, 20], [15, 30, 25], [7, 16, 15]] 


print(homersekletek[0])   


print(homersekletek[0][1])  
"""""
for nap in homersekletek:
    for meres in nap:
        print(meres)
        
homersekletek[0][1] = 22
  
   
homersekletek[0].insert(0, 0)
 
homersekletek.insert(1, [0, 0, 0])
  
    
del homersekletek[0][0]
homersekletek[0].pop(0)
  
    
del homersekletek[1]
homersekletek.pop(1)
    """""
    
    
    
