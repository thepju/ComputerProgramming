def square(n) :
	for i in range(n) :
		a.append([])
		if i == 0 or i == n-1 :	
			for j in range(n) :
				a[i].append('.')
		else :
			a[i].append('.')
			for j in range(2,n) :
				a[i].append(' ')
			a[i].append('.')
	return a
def x(m) :
	for row in range(1,m) :
		a[row].pop(row)
		a[row].insert(row,'.')
	for row in range(m-1,0,-1) :
		a[row].pop(m-row)
		a[row].insert(m-row,'.')
	return a

n = int(input())
a = []
a = square(n)
m = n-1
a = x(m)

for i in range(len(a)) :
	for j in range(len(a[i])):
		print(a[i][j],end='')
	print()

