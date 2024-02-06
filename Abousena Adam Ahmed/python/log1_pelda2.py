def kiertekeles(valasz1, valasz2):
    if valasz1.lower() == 'igen' and valasz2.lower() == 'igen':
        return "mind a ketten jönnek kosarazni"
    elif valasz1.lower() == 'nem' and valasz2.lower() == 'nem':
        return "egyikük sem jön kosarazni"
    else:
        return "csak az egyikük jön kosarazni"

valasz_henrik = input("Jön Henrik ma kosarazni? (igen/nem): ")

valasz_hanna = input("Jön Hanna ma kosarazni? (igen/nem): ")

eredmeny = kiertekeles(valasz_henrik, valasz_hanna)
print("Az eredmény: {}".format(eredmeny))