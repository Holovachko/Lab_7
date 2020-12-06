matrix = []
i = int(input('Кількість рядків = '))
j = int(input('кількість стовпців = '))

for m in range(i):
    b = []
    for m in range(j):
        b.append(float(input('Введіть елементи матриці ')))
    matrix.append(b)

for n in matrix:
    if matrix.index(n)%2 !=0:
        n.sort()
        print(n)
    else:
        continue
