price = 100 # Global scope

def increment():
  price = 200 # Local scope
  result = price + 10
  print(result)

print(price)
increment()