def plus_matrix(A,B) :
    C = zeroMat(B)
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def zeroMat(A):
    C = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(0)
        C.append(row)
    return C

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
    return C

def zeroMat2(i,j) :
    res = []
    for A in range(i):
        tmp = []
        for B in range(j):
            tmp.append(0)
        res.append(tmp)
    return res

def mul_matrix(A,B):
    C = zeroMat2(len(A),len(B[0]))
    for i in range(len(A)):
        for k in range(len(B[0])):
            for j in range(len(B)):
                C[i][k] += (A[i][j]*B[j][k])
    return C

def minus_matrix(A,B) :
    C = zeroMat(B)
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def power_matrix(A,c):
    C = A
    for i in range(c-1):
        B = zeroMat2(len(A),len(C[0]))
        for i in range(len(A)):
            for k in range(len(C[0])):
                for j in range(len(C[0])):
                       B[i][k] += A[i][j] * C[j][k]
        A = B
    return A

def transpose_matrix(A):
    B =zeroMat2(len(A[0]),len(A))
    for i in range(len(A[0])):
        for j in range(len(A)):
            B[i][j] = A[j][i] 
    return B

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

B = transpose_matrix(B)
AplusB = plus_matrix( A,B )

C = power_matrix(C,2)
CminusD = minus_matrix( C,D )

X = mul_matrix(AplusB,CminusD) 
print_matrix(X)