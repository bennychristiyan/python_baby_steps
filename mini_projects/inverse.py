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
def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
def det3x3(m):
    return m[0][0]*det2x2([[m[1][1], m[1][2]], [m[2][1], m[2][2]]]) - \
           m[0][1]*det2x2([[m[1][0], m[1][2]], [m[2][0], m[2][2]]]) + \
           m[0][2]*det2x2([[m[1][0], m[1][1]], [m[2][0], m[2][1]]])
print("\n|A| = ",det3x3(A))
print("\nthe inverse of A matrix (A^-1) is given as")
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
inv = inverse3x3(A)
for i in range(len(inv)):
    for j in range(i, len(inv)):
        inv[i][j], inv[j][i] = inv[j][i], inv[i][j]
for i in range(len(inv)):
    for j in range(len(inv[i])):
        inv[i][j] = "{:.2f}".format(inv[i][j])
A_inv = []
for i in range(len(inv)):
    float_row = []
    for j in range(len(inv[i])):
        float_row.append(float(inv[i][j]))
    A_inv.append(float_row)
print(f"[{A_inv[0][0]}  {A_inv[0][1]}  {A_inv[0][2]}]")
print(f"[{A_inv[1][0]}  {A_inv[1][1]}  {A_inv[1][2]}]")
print(f"[{A_inv[2][0]}  {A_inv[2][1]}  {A_inv[2][2]}]")








    
