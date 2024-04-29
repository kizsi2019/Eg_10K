import random
list = random.choices(range(1,200),k=50)
def maxmindiff(list):
    return max(list)-min(list)
print(maxmindiff(list))