matrix = []
i = int(input('Кількість рядків = '))
j = int(input('кількість стовпців = '))
for m in range(i):
    b = []
    for m in range(j):
        b.append(float(input('Введіть елементи матриці ')))
    matrix.append(b)
s = 0
for n in range(i):
    for m in range(j):
        if n%2==0 and  m%2==0 and matrix[n][m]<0:
            s+= matrix[n][m]
print(s)
