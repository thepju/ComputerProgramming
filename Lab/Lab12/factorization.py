def list_is_prime() :
	a = []
	for c in range(999) :
		if is_prime(c):	a.append(c)
	return a
		
def is_prime(n) :
	if n <= 1 : return False
	for i in range(2,n) :
		if n%i == 0 : return False
	return True

def print_solve(): 
	n = int(input('n: '))
	#n = 12
	for i in range(9999) :
		for j in a :
			if n%j == 0 :
				print(j,end=' ')
				n = n/j
				break

#--------------main------------------
a = list_is_prime()
print_solve()