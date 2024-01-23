print('Jöttem' + ' ' + 'láttam' + ' ' + 'győztem.')
print('ja' + 'j' * 7)

    
print(str(7.53))



sztring = 'Ismered ezt a számot?'

   
print(sztring[0])      # I
print(sztring[-1])     # ?

    # Szeletelhetjük ezeket is 
print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

   
print(len(sztring))

szamlalo=0    
for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

    
if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.')

sztring = 'Ismered ezt a számot?'
sztring[0] = 'i'
  