A = input('Input set A: ').split()
#A = '2 3 7 11 13 17 19'.split()
A1 = []
for i in range(len(A)) :
	x = int(A[i])
	A1.append(x)

B = input('Input set B: ').split()
#B = '3 5 7 9'.split()
B1 = []
for i in range(len(B)) :
	x = int(B[i])
	B1.append(int(x))

def union(A,B) : 
	C = A+B 
	C = sorted(list(set(C)))
	return C
print('A union B:',union(A1,B1))

