n,m = input('Grid Size: ').split()
n,m = int(n),int(m)
mine = int(input('Number of mine(s): '))
#n,m = 4,4
#mine = 3
position = []
for i in range(1,mine+1):
 a = input(f'Mine#{i}: ').split()
 for j in range(len(a)):
  a[j] = int(a[j])
 position.append(a)
grid = []
for i in range(m):
 row  = []
 for j in range(n):
  if([j,i] in position):
   row.append('X')
  else:
   row.append(0)
 grid.append(row)
#print(grid)
for i in range(m):
 for j in range(n):
  if(grid[i][j] == 'X'):
   if(i>=1) and (j>=1) and  (i<m-1) and (j<n-1):
    for k in range(i-1,i+2):
     for p in range(j-1,j+2):
      if(grid[k][p] != 'X'):
       grid[k][p] += 1
   elif(i == 0) and (j == 0):
    if(grid[0][1] != 'X'):
     grid[0][1] +=1
    if(grid[1][1] != 'X'):
     grid[1][1] +=1
    if(grid[1][0] != 'X'):
     grid[1][0] +=1
   elif(i == m-1) and (j == 0):
    if(grid[i-1][0] != 'X'):
     grid[i-1][0] +=1
    if(grid[i-1][1] != 'X'):
     grid[i-1][1] +=1
    if(grid[i][1] != 'X'):
     grid[i][1] +=1
   elif(i == 0) and (j == n-1):
    if(grid[0][j-1] != 'X'):
     grid[0][j-1] +=1
    if(grid[1][j-1] != 'X'):
     grid[1][j-1] +=1
    if(grid[1][j] != 'X'):
     grid[1][j] +=1
   elif(i == m-1) and (j == n-1):
    if(grid[i-1][j] != 'X'):
     grid[i-1][j] +=1
    if(grid[i][j-1] != 'X'):
     grid[i][j-1] +=1
    if(grid[i-1][j-1] != 'X'):
     grid[i-1][j-1] +=1
   elif(i ==0) and (j >=1) and (j <n-1):
    for k in range(0,2):
     for p in range(j-1,j+2):
      if(grid[k][p] != 'X'):
       grid[k][p] += 1
   elif(j == 0) and (i>=1) and (i<m-1):
    for k in range(i-1,i+2):
     for p in range(0,2):
      if(grid[k][p] != 'X'):
       grid[k][p] += 1
   elif(i ==m-1) and (j>=1) and (j<n-1):
    for k in range(i-1,i+1):
     for p in range(j-1,j+2):
      if(grid[k][p] != 'X'):
       grid[k][p] += 1
   elif(j == n-1) and (i>=1) and (i<m-1):
    for k in range(i-1,i+2):
     for p in range(j-1,j+1):
      if(grid[k][p] != 'X'):
       grid[k][p] += 1
for i in range(len(grid)):
 for j in range(len(grid[i])):
  print(grid[i][j],end=' ')
 print()