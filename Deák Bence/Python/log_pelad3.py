henrik = str(input("Henrik jön kosarazni? (i/n): "))
hanna = str(input("Hanna jön kosarazni? (i/n): "))

if henrik == "i" and hanna == "i":
    print("Mindketten jönnek.")
elif henrik == "i" and hanna == "n":
    print("Csak Henrik jön.")
elif henrik == "n" and hanna == "i":
    print("Csak Hanna jön.")
elif henrik == "n" and hanna == "n":
    print("Egyik sem jön.")
