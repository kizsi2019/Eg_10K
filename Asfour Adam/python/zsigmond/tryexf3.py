
with open("szamok.txt", "w") as file:
     file.write("10\t5")  
     def read_and_divide(filename): 
        try: 
            with open(filename, "r") as file: 
                content = file.readline() 
                numbers = content.split("\t") 
                if len(numbers) != 2: 
                    raise ValueError("A fájlban nem megfelelő formátumú adat található.") 
                num1, num2 = map(float, numbers) 
                if num2 == 0: 
                    raise ZeroDivisionError("A második szám nulla, nem lehet osztani vele.") 
                result = num1 / num2 
                print("A két szám hányadosa:", result) 
        except FileNotFoundError: print("A megadott fájl nem található.") 
        except ValueError as ve: print("Hiba:", ve) 
        except ZeroDivisionError as zde: print("Hiba:", zde)  
        
read_and_divide("szamok.txt")
