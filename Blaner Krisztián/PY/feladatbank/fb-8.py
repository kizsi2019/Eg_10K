def avrg(list):
    avrage = sum(list) / len(list)
    index = []
    for i in list:
        if i > avrage:
            index.append(i)
    r = [avrage]
    r.extend(index)
    return r
lis = [4,2,5,7,3,1,3,5,8,4,2,0,3,5,8,4,1,3,5,6,5,2,4,6]
print(avrg(lis))