def kerulet(*args):
    # Determine the number of arguments
    arg_count = len(args)
    
    if arg_count == 0:
        # Square
        side_length = args[0]
        return 4 * side_length
    elif arg_count == 1:
        # Rectangle
        length = args[0]
        breadth = args[1]
        return 2 * (length + breadth)
    elif arg_count == 2:
        # Right triangle
        a = args[0]
        b = args[1]
        return a + b + math.sqrt(a**2 + b**2)
    else:
        # Polygon
        sides = args
        perimeter = 0
        for side in sides:
            perimeter += side
        return perimeter

# Function calls for each shape type
print("Square: ", kerulet(5))
print("Rectangle: ", kerulet(5, 6))
print("Right triangle: ", kerulet(3, 4))
print("Polygon: ", kerulet(5, 3, 4, 5))