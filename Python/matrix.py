"""
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

r4=[1,2,1]
r5=[1,7,6]
r6=[2,9,3]

X,Y=[],[]
X.append(r1)
X.append(r2)
X.append(r3)
Y.append(r4)
Y.append(r5)
Y.append(r6)

print(X)
print(Y)

C=[[0 for i in range(len(X))] for i in range(len(X))]
print(C)

for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Y)):
            C[i][j]+=X[i][k]*Y[k][j]
            
print(C)
"""

"""
It initilizes matrix of n x n
"""


def initalize_matrix(n):
    matx = [[0 for _ in range(n)] for _ in range(n)]
    return matx


"""
Finds dot product of matrices
"""


def dot_product(m, n):
    dim = len(m)
    ans = 0
    for i in range(dim):
        ans += m[i] * n[i]
    return ans


"""
It gives the ith row
"""


def row(matx, i):
    dim = len(matx)
    row = []
    for k in range(dim):
        row.append(matx[i][k])
    return row


"""
It gives the ith column
"""


def column(matx, j):
    dim = len(matx)
    column = []
    for k in range(dim):
        column.append(matx[k][j])
    return column


"""
Calculates matrix multiplication
"""


def matrix_multiplication(A, B):
    dim = len(A)
    C = initalize_matrix(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A, i), column(B, j))
    return C


"""
Driver code
"""
X, Y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 1], [1, 7, 6], [2, 9, 3]]
print(X)
print(Y)
print(matrix_multiplication(X, Y))
