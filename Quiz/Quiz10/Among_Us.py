n = int(input("Input n: "))
m = int(input("Input m: "))
#n = 2
#m = 5

unlock = []
for i in range(n):
		un  = input().strip().split()
		unlock.append(un)

for num in range(1,n*m+1,1):
	for i in range(n):
		for j in range(m):
			if int(unlock[i][j]) == num :
				print(f'({i},{j})')