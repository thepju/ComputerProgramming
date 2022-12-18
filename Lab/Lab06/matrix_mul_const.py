def mul_const(A,c):
	C = zeroMat(A)
	for i in range(len(A)):
		for j in range(len(A[i])):
			C[i][j] = c*A[i][j]
	return C

def print_matrix(A):
	for i in range(len(A)):
		for j in range(len(A[i])):
			print(f'{A[i][j]:^6}', end = ' ')
		print()


def zeroMat(A):
  C = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[i])):
      row.append(0)
    C.append(row)
  return C

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2


C = mul_const(A,c)
print_matrix(C)
