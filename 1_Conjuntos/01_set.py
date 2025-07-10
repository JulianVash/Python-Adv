from enum import unique


set_countries = {"spain", "france", "germany", "norway"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 34, 5,5,5}
print(set_numbers)

set_types = {1, "hi", (1,2,3),False}
print(set_types)

set_from_string = set("hello")
print(set_from_string)

set_from_tuples = set(("abc", "bcd", "abc", "abc"))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4,5,3,1,12,2,3]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)