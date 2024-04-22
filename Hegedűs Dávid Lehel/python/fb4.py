def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg = average(numbers)
print(avg) 