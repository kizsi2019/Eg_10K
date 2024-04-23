import random
list = random.choices(range(1,200),k=50)
def aboveavr(list):
    x = sum(list)/len(list)
    return [y for y in list if y > x]
print(sorted(aboveavr(list)))