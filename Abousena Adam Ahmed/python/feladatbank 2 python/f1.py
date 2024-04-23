'''1. Készíts egy függvényt, amely egy adott számlistát vár bemenetként, majd visszaadja az összes páros számot a listában.'''
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print(get_even_numbers(numbers))  


