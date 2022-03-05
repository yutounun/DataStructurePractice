data = [3,4,5,2,6,0,7,9,8]
num = len(data)

for i in range(num-1):
  for j in range(num-1, i, -1):
    if data[j-1] > data[j]:
      data[j], data[j-1] = data[j-1], data[j]

print(data, "sorted data")
