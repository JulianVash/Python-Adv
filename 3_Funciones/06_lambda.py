def increment(x):
  return x + 1

result = increment(10)
print(result)

increment_v2 = lambda x : x + 1
result_v2 = increment_v2(20)
print(result_v2)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
print(full_name('julian', 'gonzalez'))