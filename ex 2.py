n = int(input('n = '))
m = int(input('m = '))
matrix = []
num = 1
q = 0
for i in range(n):
    b = []
    for j in range(m):
        if (j * i) % 2 == 0:
            for r in range(m+1):
                num *= r
            b.append(num)
        else:
            for r in range (n + 1):
                q += r
            b.append(q)
    matrix.append(b)
print(matrix)

list1 = []
for k in matrix:
    list1.extend(k)
print(list1)
