
#3. rész
class ShipData:
    def __init__(self,name,vizbocs,tname,maxdistance):
        self.name = name
        self.vizbocs = int(vizbocs)
        self.tname = tname
        self.maxdistance = int(maxdistance)

shiplist = []
with open("ship.txt", "r") as f:
    file = f.readlines()
    file.pop(0)
    file.pop(0)
    for i in file:
        a = i.strip().split(";")
        b = ShipData(a[0],a[1],a[2],a[3])

        shiplist.append(b)

m = 2024
for i in shiplist:
    a = i.vizbocs
    if a < m:
        m = a

for i in shiplist:
    if i.vizbocs == m:
        forraselso = i
        break
print(forraselso.name)

def atlagtav(shiplist):
    ossz = 0
    for i in shiplist:
        ossz += i.maxdistance
    return round(ossz/len(shiplist),2)
after1980 = [i for i in shiplist if i.vizbocs > 1980]
print(atlagtav(after1980))