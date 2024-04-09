try:
    with open('numbers.txt', 'r') as f:
      
        line = f.readline().strip()

        
        nums = line.split('\t')
        num1 = float(nums[0])
        num2 = float(nums[1])

       
        quotient = num1 / num2

        
        print(f"a hanyadosa {num1} és {num2} az {quotient}.")

except FileNotFoundError:
    print("Error: a fájl nem található(numbers.txt).")


except ValueError:
    print("Error: nem tartalmmaz jo szamot.")