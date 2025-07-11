numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda i: i % 2 == 0, numbers))
print(new_numbers)
print(numbers)