mazeSize = int(input("Input the maze's size (only 1 to 9): "))
typeMaze = int(input("Input the type of maze (only 1 to 2): "))

size = 2*mazeSize-1

a = [ [0]*size for i in range(size) ]
x = 0
y = size
if typeMaze == 1 :
	for r in range(1,mazeSize+1,2):
		for i in range(x,y):
			for j in range(x,y):
				a[i][j] = r
		x += 1
		y -= 1 

	for r in range(2,mazeSize+1,2):
		for i in range(x,y):
			for j in range(x,y):
				a[i][j] = r
		x += 1
		y -= 1 

#print(a)

if typeMaze == 2 :

	for r in range(2,mazeSize+1,2):
		for i in range(x,y):
			for j in range(x,y):
				a[i][j] = r
		x += 1
		y -= 1 
	for r in range(1,mazeSize+1,2):
		for i in range(x,y):
			for j in range(x,y):
				a[i][j] = r
		x += 1
		y -= 1 

for i in range(len(a)):
	for j in range(len(a)):
		print(a[i][j],end =' ')
	print()