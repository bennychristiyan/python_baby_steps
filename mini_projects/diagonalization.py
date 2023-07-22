n = int(input("Enter the size of the matrix: "))
A = []
print("\nEnter the elements of the matrix, row by row:")
for i in range(n):
    list = []
    for j in range(n):
        a = int(input(f"enter the number for a{i+1}{j+1}: "))
        list.append(a)
    A.append(list)
print("\nthe A matrix is given as: ")
print(f"[{A[0][0]}  {A[0][1]}  {A[0][2]}]")
print(f"[{A[1][0]}  {A[1][1]}  {A[1][2]}]")
print(f"[{A[2][0]}  {A[2][1]}  {A[2][2]}]")
trace = 0
for i in range(n):
    for j in range(n):
        if i==j:
            trace += A[i][j]
print("\ntrace(A) = ",trace)
def minor(matrix):
    n= len(matrix)
    minors = []
    for i in range(n):
        diag_element = matrix[i][i]
        minor_matrix = []
        for j in range(n):
            if j != i:
                a = matrix[j][:i] + matrix[j][i+1:]
                minor_matrix.append(a)
        minor_det = determinant(minor_matrix)
        minors.append(minor_det)
    return minors
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for i in range(n):
            minor_matrix = []
            for j in range(1, n):
                minor_row = matrix[j][:i] + matrix[j][i+1:]
                minor_matrix.append(minor_row)
            sign = (-1)**i
            cofactor = sign*determinant(minor_matrix)
            det += matrix[0][i]*cofactor
        return det
minor_values = minor(A)
sum_diagonal_minors = sum(minor_values)
print("the sum of minors of the diagonal elements = ",sum_diagonal_minors)
def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            sign = (-1) ** j
            submatrix = []
            for i in range(1, n):
                row = []
                for k in range(n):
                    if k != j:
                        row.append(matrix[i][k])
                submatrix.append(row)
            cofactor = sign * det(submatrix)
            determinant += matrix[0][j] * cofactor
    return determinant
print("|A| = ", det(A))
print("\nthe characteristic equation is |A-λI| = 0")
print(f"(i.e) λ³ - {trace}λ² + {sum_diagonal_minors}λ - {det(A)} = 0 ")
import numpy as np
a = 1
b = -1*trace
c = sum_diagonal_minors
d = -1*det(A)
p = [a,b,c,d]
_λ = np.roots(p)
_λ1 = round(_λ[0])
_λ2 = round(_λ[1])
_λ3 = round(_λ[2])
print("\nthe eigen values are ",_λ1, _λ2, _λ3)
print("                                [x1]")
print("eigen vector is, X = [x2]")
print("                                [x3]\n")
print("(A-λI)X = 0")
print(f"[{A[0][0]}-λ  {A[0][1]}     {A[0][2]}   ][x1]")
print(f"[{A[1][0]}     {A[1][1]}-λ  {A[1][2]}   ][x2]")
print(f"[{A[2][0]}     {A[2][1]}     {A[2][2]}-λ][x3]")
B = []
l = []
m = []
n = []
print("\ncase1: λ=",_λ1)
A[0][0] = A[0][0] - _λ1
A[1][1] = A[1][1] - _λ1
A[2][2] = A[2][2] - _λ1
print(f"[{A[0][0]}  {A[0][1]}  {A[0][2]}][x1]")
print(f"[{A[1][0]}  {A[1][1]}  {A[1][2]}][x2]")
print(f"[{A[2][0]}  {A[2][1]}  {A[2][2]}][x3]")
x1 = (A[0][1]*A[1][2])-(A[1][1]*A[0][2])
x2 = (A[0][0]*A[1][2])-(A[1][0]*A[0][2])
x3 = (A[0][0]*A[1][1])-(A[1][0]*A[0][1])
print(f"       [{x1}]")
print(f"X1= [{-1*x2}]")
print(f"       [{x3}]")
l.append(x1)
l.append(-1*x2)
l.append(x3)
B.append(l)
print("\ncase2: λ=",_λ2)
A[0][0] = A[0][0] + _λ1
A[1][1] = A[1][1] + _λ1
A[2][2] = A[2][2] + _λ1
A[0][0] = A[0][0] - _λ2
A[1][1] = A[1][1] - _λ2
A[2][2] = A[2][2] - _λ2
print(f"[{A[0][0]}  {A[0][1]}  {A[0][2]}][x1]")
print(f"[{A[1][0]}  {A[1][1]}  {A[1][2]}][x2]")
print(f"[{A[2][0]}  {A[2][1]}  {A[2][2]}][x3]")
x1 = (A[0][1]*A[1][2])-(A[1][1]*A[0][2])
x2 = (A[0][0]*A[1][2])-(A[1][0]*A[0][2])
x3 = (A[0][0]*A[1][1])-(A[1][0]*A[0][1])
print(f"       [{x1}]")
print(f"X2= [{-1*x2}]")
print(f"       [{x3}]")
m.append(x1)
m.append(-1*x2)
m.append(x3)
B.append(m)
print("\ncase3: λ=",_λ3)
A[0][0] = A[0][0] + _λ2
A[1][1] = A[1][1] + _λ2
A[2][2] = A[2][2] + _λ2
A[0][0] = A[0][0] - _λ3
A[1][1] = A[1][1] - _λ3
A[2][2] = A[2][2] - _λ3
print(f"[{A[0][0]}  {A[0][1]}  {A[0][2]}][x1]")
print(f"[{A[1][0]}  {A[1][1]}  {A[1][2]}][x2]")
print(f"[{A[2][0]}  {A[2][1]}  {A[2][2]}][x3]")
x1 = (A[0][1]*A[1][2])-(A[1][1]*A[0][2])
x2 = (A[0][0]*A[1][2])-(A[1][0]*A[0][2])
x3 = (A[0][0]*A[1][1])-(A[1][0]*A[0][1])
print(f"       [{x1}]")
print(f"X3= [{-1*x2}]")
print(f"       [{x3}]")
n.append(x1)
n.append(-1*x2)
n.append(x3)
B.append(n)
for i in range(len(B)):
    for j in range(i, len(B)):
        B[i][j], B[j][i] = B[j][i], B[i][j]
print("\nthe model matrix B is")
print(f"[{B[0][0]}  {B[0][1]}  {B[0][2]}]")
print(f"[{B[1][0]}  {B[1][1]}  {B[1][2]}]")
print(f"[{B[2][0]}  {B[2][1]}  {B[2][2]}]")
print("\nB^-1 is given as")
def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def det3x3(m):
    return m[0][0]*det2x2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]) - \
           m[0][1]*det2x2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]) + \
           m[0][2]*det2x2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])
def cofactor(m):
    return [[det2x2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]), -det2x2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]),\
             det2x2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])],
            [-det2x2([[m[0][1], m[0][2]], [m[2][1], m[2][2]]]), det2x2([[m[0][0], m[0][2]], [m[2][0], m[2][2]]]),\
             -det2x2([[m[0][0], m[0][1]], [m[2][0], m[2][1]]])],
            [det2x2([[m[0][1], m[0][2]], [m[1][1], m[1][2]]]), -det2x2([[m[0][0], m[0][2]], [m[1][0], m[1][2]]]),\
             det2x2([[m[0][0], m[0][1]], [m[1][0], m[1][1]]])]]
def inverse3x3(m):
    det = det3x3(m)
    if det == 0:
        return None
    else:
        c = cofactor(m)
        adj = [[c[i][j]/det for j in range(3)] for i in range(3)]
        return adj
inv = inverse3x3(B)
for i in range(len(inv)):
    for j in range(i, len(inv)):
        inv[i][j], inv[j][i] = inv[j][i], inv[i][j]
for i in range(len(inv)):
    for j in range(len(inv[i])):
        inv[i][j] = "{:.2f}".format(inv[i][j])
B_inv = []
for i in range(len(inv)):
    float_row = []
    for j in range(len(inv[i])):
        float_row.append(float(inv[i][j]))
    B_inv.append(float_row)
print(f"[{B_inv[0][0]}  {B_inv[0][1]}  {B_inv[0][2]}]")
print(f"[{B_inv[1][0]}  {B_inv[1][1]}  {B_inv[1][2]}]")
print(f"[{B_inv[2][0]}  {B_inv[2][1]}  {B_inv[2][2]}]")
A[0][0] = A[0][0] + _λ3
A[1][1] = A[1][1] + _λ3
A[2][2] = A[2][2] + _λ3
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(B_inv)):
    for j in range(len(A[0])):
        for k in range(len(A)):
            result[i][j] += B_inv[i][k] * A[k][j]
D = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(result)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            D[i][j] += result[i][k] * B[k][j]
for i in range(3):
    for j in range(3):
        D[i][j] = round(D[i][j])
print("\nthe diagonalized matrix D is given as")
print(f"[{D[0][0]}  {D[0][1]}  {D[0][2]}]")
print(f"[{D[1][0]}  {D[1][1]}  {D[1][2]}]")
print(f"[{D[2][0]}  {D[2][1]}  {D[2][2]}]")




















    






