def max_number(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_num = max_number(numbers)
print(max_num)  