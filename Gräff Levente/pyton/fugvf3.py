def harommal_oszthatok(number_list):
    count = 0
    for num in number_list:
        if num % 3 == 0:
            count += 1
        return count

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print(harommal_oszthatok(numbers))


def harommal_oszthatok(number_list):
    count = 0
    for num in number_list:
        if num % 3 == 0:
            count += 1
    return count

numbers = []
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    numbers.append(num)

print(harommal_oszthatok(numbers))