
#1. rész
u = input("Adja meg a hajó nevét és gyártási évét(név, év)>>>")
while True:
    u = u.split(", ")
    try:
        if int(u[1]) > 1950 and int(u[1]) < 2024:
            break
        else:
            u = input("Adja meg a hajó nevét és gyártási évét(név, év)>>>")
    except:
        u = input("Adja meg a hajó nevét és gyártási évét(név, év)>>>")

print(f"név: {u[0]}, hossz: {len(u[0])}\nkor: {u[1]}")

