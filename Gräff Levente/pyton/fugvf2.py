def paros_e(number_list):
   for num in number_list:
       if num % 2 == 0:
           return True
   return False

numbers = [1, 4, 5, 7, 8]
print(paros_e(numbers))