a = []

for i in range(1,4):
 p = input('Row %d : '%i).split()
 for j in range(3):
  p[j] = int(p[j])
 a.append(p)

for i in range(len(a)):
 for j in range(len(a[i])):
  a[i].append(a[i][j])

#main
up = down = 0
for i in range(3):
 up += a[0][i] * a[1][i+1] * a[2][i+2]
for i in range(3):
 down += a[2][i] * a[1][i+1] * a[0][i+2]

final = up - down
print(final)