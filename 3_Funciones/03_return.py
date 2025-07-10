def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, "hola"

result = find_volume(width=10)
print(result)

result = find_volume(10, 20, 30)
print(result)
print(result[2])

result, width, text = find_volume(10, 20, 30)
print(text)