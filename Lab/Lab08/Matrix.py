#elab 8

def readall(filename) :
	with open(filename,'r') as f:
		f_contents = f.readlines() 
	alldata = []
	for i in f_contents :
		if i != '' :
			tmp = []
			for j in i.strip().split():
				tmp.append(j)
			alldata.append(tmp)

	return alldata

def readmat(alldata) :
	allmat = []
	mat = []

	for i in alldata :
		if len(i) > 1 :
			smallmat = []
			for j in range(len(i)) : #convert str to integer
				smallmat.append(int(i[j]))
			mat.append(smallmat)
		elif len(i) == 1 : #operator
			allmat.append(mat)
			mat = []
			allmat.append(i)
		if i == alldata[-1] :
			if len(i) > 1 :		allmat.append(mat)
			else :	continue
	return allmat

def plus(A,B):
     return [[A[i][j]+B[i][j] for j in range(len(A[0])) ] for i in range(len(A))]

def multiply(A,B):
     return [ [ sum([ (A[i][k] * B[k][j])  for k in range(len(A[0]))]) for j in range(len(B[0])) ] for i in range(len(A))  ]

def calmat(allmat) :
	Round = 0
	result = []
	for i in allmat:
		#print('i is ',i)
		if len(i) != 1 :
			if Round == 0 :
				mat1 = i
				Round += 1
				#print(mat1)
			else :
				mat2 = i
				#print(mat2)
				if opera == '*' :	
					result = multiply(mat1,mat2)
				else :	
					result = plus(mat1,mat2)
				mat1 = result
		else :
			if i[0] == '*' : #convert list to str
				opera = '*'
			else :	
				opera = '+'
	return result

filename = input('File name: ')
#filename = 'matrix.txt'

alldata = readall(filename)
allmat = readmat(alldata)
#print(allmat)
result = calmat(allmat)

for i in range(len(result)):
    for j in range(len(result[0])):
        print(f"{result[i][j]:^5}",end=" ")
    print()


