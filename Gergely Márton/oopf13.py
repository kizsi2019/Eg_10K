def calculate_square_properties(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter
6
squares = []
while True:
    side = int(input("Enter the side length of a square (0 to stop): "))
    if side == 0:
        break
    squares.append(side)

print("\nSide Lengths:")
for side in squares:
    print(side, end=" ")

print("\n\nAreas:")
for side in squares:
    area, _ = calculate_square_properties(side)
    print(area)

print("\nPerimeters:")
for side in squares:
    _, perimeter = calculate_square_properties(side)
    print(perimeter)