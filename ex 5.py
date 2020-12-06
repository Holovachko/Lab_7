matrix = []
i = int(input('Кількість рядків = '))
j = int(input('кількість стовпців = '))
for m in range(i):
    b = []
    for m in range(j):
        b.append(float(input('Введіть елементи матриці ')))
    matrix.append(b)
q = 0
if i != j:
    for u in matrix:
        print(u)
        for l in u:
            if l == 0:
                q+= 1
                break
            else:
                continue
else:
    print("Ця матриця не є прямокутною")
print('кількість рядків матриці без 0 = {0}'.format(i - q))
