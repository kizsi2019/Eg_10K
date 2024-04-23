filename = "szamok.txt"

try:
    with open(filename, "r") as file:
        content = file.read()

    numbers = content.split("\t")

    if len(numbers) != 2 or not all(num.replace(".", "", 1).isdigit() for num in numbers):
        raise ValueError("The file does not contain two numbers separated by a tab character.")

    num1, num2 = map(float, numbers)

    print(f"The quotient of the two numbers: {num1 / num2}")

except FileNotFoundError:
    print(f"The {filename} file was not found!")
except ValueError as e:
    print(f"An error occurred while processing the file: {e}")