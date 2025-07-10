numbers = []
# iterate over a range of numbers
for i in range(1, 11):
    numbers.append(i * 2)

print(numbers)

# list comprehension
numbers_v2 = [element for element in range(1, 11)]  
print(numbers_v2)

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)
      
# list comprehension with conditionals
numbers_v3 = [i * 2 for i in range(1, 11) if i % 2 == 0] 
print(numbers_v3)