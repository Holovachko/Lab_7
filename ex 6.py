matrix = []
i = int(input('Кількість рядків = '))
j = int(input('кількість стовпців = '))

for m in range(i):
    b = []
    for m in range(j):
        b.append(int(input('Введіть елементи матриці ')))
    matrix.append(b)
new_list = []
for i in matrix:
    new_list.extend(i)
    
m = max([el for el in new_list if new_list.count(el)>1])
print(m)
