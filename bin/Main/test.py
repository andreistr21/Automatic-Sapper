rows = 3
columns = 5

small_image_array = [[0 for i in range(rows)] for j in range(columns)]

for el in small_image_array:
    print(el)

small_image_array[2][1] = 2

print()
for el in small_image_array:
    print(el)

