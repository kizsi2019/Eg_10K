# a visszaadja alatt azt értem hogy return, nem azt hogy ki írja
def evenfromlist(list):
    evenlist = []
    for i in list:
        if i % 2 == 0:
            evenlist.append(i)
    return evenlist

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(evenfromlist(list))