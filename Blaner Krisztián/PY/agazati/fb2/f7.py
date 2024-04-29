import random
list = random.choices(range(1,200),k=50)
print(list)
def reverser(list: list):
    list.reverse()
    return list
print(reverser(list))