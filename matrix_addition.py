a = [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ]
b = [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ]


def matrix_addition(a, b):
    c=a
    for row in range(len(a)):
        for col in range(len(a)):
            c[row][col]+= b[row][col]
    return c

print(matrix_addition(a,b))


################################################

for row in range(len(a)):
    for col in range(len(a[0])):
        result[row][col] = a[row][col] + b[row][col]
