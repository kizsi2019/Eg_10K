list = [137,613,751,37,13,7517,375,31,713,75,13713,7,13752,791,737,53,7512,7,3,793,17,538,3752,75,3741,7,52,7,7,375,27,1,72,7,275,7]
def evennums(numbers):
    return [x for x in numbers if x % 2 == 0]
print(evennums(list))