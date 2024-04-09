def range_of_numbers(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range_of_numbers = range_of_numbers(numbers)
print(range_of_numbers) 