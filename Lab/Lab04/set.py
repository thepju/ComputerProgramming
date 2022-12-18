#a = '2 3 5 7 11 13 17 19 23'
a = input('Input setA: ')
a = a.split()
A = []
for i in range(len(a)) :
	A.append(int(a[i]))
	A.sort()
len_A = len(A)

#b = '3 5 7 9'
b = input('Input setB: ')
b = b.split()
B = []
for i in range(len(b)) :
	B.append(int(b[i]))
	B.sort()
len_B = len(B)

list_inter = []
def intersect(A,B) :
	for i in range(len_A) :
		for j in range(len_B):
			if A[i] == B[j] :
				list_inter.append(A[i])
	list_inter.sort()
	print('A intersect B: ',end='')
	if list_inter != [] :
		for i in range(len(list_inter)) :
			print(list_inter[i],end=' ')
		print()
	else :
		print('empty set')
intersect(A,B)

list_AmB = []
def minus(A,B) :
	for i in range(len_A):
		res = -1
		for j in range(len_B):
			if A[i] == B[j] :
				res = 0
				break
		if res == -1 :
			list_AmB.append(A[i])
	list_AmB.sort()
	print('A minus B: ',end='')
	if list_AmB != [] :
		for i in range(len(list_AmB)) :
			print(list_AmB[i],end=' ')
		print()
	else :
		print('empty set')
minus(A,B)

list_BmA = []
def minus(B,A) :
	for i in range(len_B):
		res = -1
		for j in range(len_A):
			if B[i] == A[j] :
				res = 0
				break
		if res == -1 :
			list_BmA.append(B[i])
	list_BmA.sort()
	print('B minus A: ',end='')
	if list_BmA != [] :
		for i in range(len(list_BmA)) :
			print(list_BmA[i],end=' ')
		print()
	else :
		print('empty set')
minus(B,A)

list_union = []
def union(A,B) :
	list_union = A+B
	list_union.sort()
	list_union = set(list_union)
	list_union = list(list_union)
	print('A union B: ',end='')
	for i in range(len(list_union)) :
		print(list_union[i],end=' ')
union(A,B)
