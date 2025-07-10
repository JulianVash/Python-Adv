def sum_with_range(min, max):
  sum = 0
  
  for x in range(min, max):
    sum += x
    
  print(sum)
  return sum

print(f"Resultado = {sum_with_range(1, 10)}")
calc_value = sum_with_range(1, 10)
sum_with_range(calc_value, 100)
 