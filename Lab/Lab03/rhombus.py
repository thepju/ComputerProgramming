n = int(input('input: '))

for i in range(1,n+1,2) :
	x = n-i
	for z in range(x//2):
		print(' ',end='')
	for y in range(1) :
		print('#'*i,end='')
	for z in range(x//2):
		print(' ',end='')
	print()
  	
for i in range(n-2,0,-2) :
  x = n - i
  for z in range(x//2):
    print(' ',end='')
  for y in range(1) :
    print('#'*i,end='')
  for z in range(x//2):
    print(' ',end='')
  print()