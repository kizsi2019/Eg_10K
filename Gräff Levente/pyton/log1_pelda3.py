szam = int(input("adj szam"))
if szam % 3==0:
    print("3mal osztható")
if szam % 4==0:
    print("4 osztható")
if szam % 3==0 and szam % 4==0 :
    print("3,4 osztható")
if not szam % 3==0 or szam % 4==0:
    print("nem ostható")

