def zeromat(n,m):
 a = []
 for i in range(n):
  b=[]
  for j in range(m):
   b.append(0)
  a.append(b)
 return a

#n,m = 4,5

#c = [[2,3,5,6,2],[1,3,4,7,1],[6,5,4,1,3],[2,3,7,9,6]]

n,m = input('City Size: ').split()
n = int(n)
m = int(m)
c = zeromat(n,m)
for i in range(n):
 num = input('').split()
 for j in range(m):
  c[i][j] += int(num[j])

a = ['N','S','E','W']
b = []
#N
Ncount = 5
for i in range(m):
 for j in range(n):
  if(j == n-1):
   break
  elif(c[j][i] < c[j+1][i]):
   Ncount +=1
b.append(Ncount)
#S
Scount = 5
for i in range(m-1,-1,-1):
 for j in range(n-1,-1,-1):
  if(j == 0):
   break
  elif(c[j][i] < c[j-1][i]):
   Scount +=1
b.append(Scount)
#E
Ecount = 5
for i in range(n-1,-1,-1):
 for j in range(m-1,-1,-1):
  if(j == 0):
   break
  elif(c[i][j] < c[i][j-1]):
   Ecount +=1
b.append(Ecount)
#W
Wcount = 5
for i in range(n):
 for j in range(m):
  if(j == n-1):
   break
  elif(c[i][j] < c[i][j+1]):
   Wcount +=1
b.append(Wcount)

mymax = max(b)
for i in range(len(b)):
 if(b[i] == mymax):
  print(a[i],end=' ')