deg = float(input('degree: ')) 
x = (deg/180)*3.14
sum_sinx = 0
sum_cosx = 0

def factorial_cosx(n) :
	factorial = 1
	for i in range(1,(2*n)+1) : 
		factorial = factorial * i
	return factorial
def factorial_sinx(n) :
	factorial = 1
	for i in range(1,(2*n)) : 
		factorial = factorial * i
	return factorial

for j in range(0,11) :
	if j != 0 :
		cosx = ((-1 )**j)*(x**(2*j)) / factorial_cosx(j) 
	else :
		cosx = ((-1 )**j)*(x**(2*j)) 
	sum_cosx += cosx

for k in range(1,11) :
	if k != 0 :		
		sinx = ((-1)**(k-1))*(x**((2*k)-1)) / factorial_sinx(k)
	sum_sinx += sinx
print(f'sin({deg:.2f}): {sum_sinx:.10f}')
print(f'cos({deg:.2f}): {sum_cosx:.10f}')