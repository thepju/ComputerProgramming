def minus_matrix(A,B) :
	C = zeroMat(B)
	for i in range(len(A)):
		for j in range(len(B)):
			C[i][j] = A[i][j] - B[i][j]
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


A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[22,13,23], [54,43,21], [23,78,71]]

C = minus_matrix(A,B)
print_matrix(C)
