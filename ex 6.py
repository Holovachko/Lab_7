matrix = []
i = int(input('Кількість рядків = '))
j = int(input('кількість стовпців = '))

for m in range(i):
    b = []
    for m in range(j):
        b.append(int(input('Введіть елементи матриці ')))
    matrix.append(b)

y = 0
r = 0
if i != j:
    for x in matrix:
        for l in x:
            if y == l:
                r = l
            elif y < l:
                y = l
            else:
                continue
else:
    print('Ця матриця не є прямокутною')
print(r)
