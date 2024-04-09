
numbers = []


for i in range(3):
   
    num = input(f"Enter integer #{i+1}: ")

    try:
        
        num = int(num)
    except ValueError:
       
        print("Invalid input. Please enter an integer.")
        continue

   
    numbers.append(num)


print("The numbers you entered are:")
for num in numbers:
    print(num)