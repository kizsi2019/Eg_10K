userint = int(input("Kérek egy számot: "))

if userint > 0 and userint % 2 == 0:
    print("Ügyes! A beírt szám pozitív és páros is egyszerre! OwO")
elif userint < 0 and userint % 2 != 0:
    print("Ügyes! A beírt szám negatív és páratlan is egyszerre! OwO")
else:
    print("A beírt szám nulla. UwU")
