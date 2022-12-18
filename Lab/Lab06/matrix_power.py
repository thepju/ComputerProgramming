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
def mul_matrix(A,B):
	C = zeroMat(A)
	for i in range(len(A)):
		for k in range(len(A[i])):
			mysum = 0
			for j in range(len(A[k])):
				mysum += (A[i][j]*B[j][k]) 
			C[i][k] = mysum
	return C
def power_matrix(A,c):
	C = A
	for i in range(c-1):
		C = mul_matrix(A,C)
	return C
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
C = power_matrix(A,c)
print_matrix(C)


