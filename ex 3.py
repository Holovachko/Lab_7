matrix = []
i = 2
j = 2
for m in range(i):
    b = []
    for m in range(j):
        b.append(float(input('Введіть елементи матриці ')))
    matrix.append(b)
det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
print('Детермінант матриці = ', det)
