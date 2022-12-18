y = int(input('Input: '))
a = 0

def fac(num) :
	factorial = 1
	if num != 0 :
		for i in range(1,num+1):
			factorial = i*factorial
	else :
		factorial = 1
	return factorial

if y == 0 or y == 1 :
	print('1 ')
else :
	print('1 ')
	print('1 1 ')
	for j in range(3,y+1):
		for i in range(0,j) :
			a = int(fac(j-1) / (fac(i)*fac(j-1-i)))
			print(f'{a} ',end='')
		print()	
		

